import yaml
import jinja2
import os
from wordcloud import WordCloud
import argparse


CLOUD_FILE_NAME="cloud.png"
GITHUB_URL="https://github.com/lukaszkuczynski/search_my_bio"
PROFILE_FILE_NAME="profiles.yml"

def jinja_render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context=context)


def cloud(doc):
    tags = []
    for project in doc['Projects']['Commercial']:
        if 'technologies' in project:
            tags.extend([x for x in project['technologies']])
    # for project_name in doc['Projects']['Private']:
    #     if 'technologies' in doc['Projects']['Private'][project_name]:
    #         tags.extend([x for x in doc['Projects']['Private'][project_name]['technologies']])
    wc = WordCloud(background_color="white", max_words=2000, contour_width=3, contour_color='steelblue')
    wc.generate(' '.join(tags))
    wc.to_file(CLOUD_FILE_NAME)


def filter_projects_if_needed(projects, params):
    if params.profile:
        with open(PROFILE_FILE_NAME, encoding='utf8') as f:
            profile_name = params.profile
            doc = yaml.load(f, Loader=yaml.FullLoader)
            if not profile_name in doc:
                raise Exception("Profile '%s' is not available in a profiles definition file." % profile_name)
            active_projects = ()
            all_project_names = set(project['name'] for project in projects)
            if 'active' in doc[profile_name]:
                active_projects_names = set(doc[profile_name]['active'])
                filtered = [project for project in projects if project['name'] in active_projects_names]
            if 'inactive' in doc[profile_name]:
                inactive_projects_names = set(doc[profile_name]['inactive'])
                filtered = [project for project in projects if project['name'] not in inactive_projects_names]
            filtered_names = set(project['name'] for project in filtered)
            irrelevant_names = all_project_names - filtered_names
            irrelevant = [project for project in projects if project['name'] in irrelevant_names]
            return filtered, irrelevant
    else:
        return projects


def generate(params):
    fname = args.file
    fname_out = "out_cv.html"
    with open(fname, encoding='utf8') as f:
        doc = yaml.load(f, Loader=yaml.FullLoader)
        commercial_original = doc['Projects']['Commercial']
        commercial, commercial_irrelevant = filter_projects_if_needed(commercial_original, params)
        private_original = doc['Projects']['Private']
        private, private_irrelevant = filter_projects_if_needed(private_original, params)
        # commercial_projects_hidden = len(commercial_original) - len(commercial)
        # private_projects_hidden = len(private_original) - len(private)
        cloud(doc)
        context = {
            'commercial_projects' : commercial,
            'private_projects': private,
            'courses': doc['Education']['courses'],
            'general': doc['General'],
            'project_url': GITHUB_URL,
            'skill_cloud_url': CLOUD_FILE_NAME,
            'commercial_projects_irrelevant': commercial_irrelevant,
            'private_projects_irrelevant': private_irrelevant,
        }
        out = jinja_render('./full_cv_template.html', context)
        with open(fname_out, 'wb') as fout:
            fout.write(out.encode('utf-8'))


# def arguments():

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--profile", help="profile, which will filter projects according to the application needs")
    parser.add_argument("-f", "--file", help="YAML path containing your projects", default='life_tasks.yml')
    args = parser.parse_args()
    generate(args)
