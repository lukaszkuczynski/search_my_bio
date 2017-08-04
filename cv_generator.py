import yaml
import jinja2
import os


def jinja_render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context=context)


def generate():
    fname = "life_tasks.yml"
    fname_out = "out_cv.html"
    with open(fname) as f:
        doc = yaml.load(f)
        commercial = doc['Projects']['Commercial']
        private = doc['Projects']['Private']
        context = {
            'commercial_projects' : commercial,
            'private_projects': private,
            'schools': doc['Education']['schools']
        }
        out = jinja_render('./full_cv_template.html', context)
        print(out)
        with open(fname_out, 'w') as fout:
            fout.write(out)

generate()
