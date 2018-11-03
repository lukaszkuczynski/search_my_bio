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
            doc = yaml.load(f)
            if not profile_name in doc:
                raise Exception("Profile '%s' is not available in a profiles definition file." % profile_name)
            print(doc[profile_name])
            active_projects = set(doc[profile_name]['active'])
            filtered = [project for project in projects if project['name'] in active_projects]
            return filtered
    else:
        return projects


def generate(params):
    fname = "life_tasks.yml"
    fname_out = "out_cv.html"
    with open(fname, encoding='utf8') as f:
        doc = yaml.load(f)
        commercial_original = doc['Projects']['Commercial']
        commercial = filter_projects_if_needed(commercial_original, params)
        private_original = doc['Projects']['Private']
        private = filter_projects_if_needed(private_original, params)
        commercial_projects_hidden = len(commercial_original) - len(commercial)
        private_projects_hidden = len(private_original) - len(private)
        skill_cloud = cloud(doc)
        context = {
            'commercial_projects' : commercial,
            'private_projects': private,
            'schools': doc['Education']['schools'],
            'general': doc['General'],
            'project_url': GITHUB_URL,
            'skills': skill_cloud,
            'skill_cloud_url': CLOUD_FILE_NAME,
            'commercial_projects_hidden': commercial_projects_hidden,
            'private_projects_hidden': private_projects_hidden,
        }
        out = jinja_render('./full_cv_template.html', context)
        print(out)
        with open(fname_out, 'wb') as fout:
            fout.write(out.encode('utf-8'))


# def arguments():

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--profile", help="profile, which will filter projects according to the application needs")
    args = parser.parse_args()
    generate(args)
