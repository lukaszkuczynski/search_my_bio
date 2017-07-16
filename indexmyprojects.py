import yaml
from elasticsearch import Elasticsearch

def projects_from_file(fname):
    with open(fname) as f:
        doc = yaml.load(f)
        commercial = doc['Projects']['Commercial']
        for project in commercial.keys():
            yield (project, commercial[project])
        private = doc['Projects']['Private']
        for project in private.keys():
            yield (project, private[project])

fname = "projects.yml"

es = Elasticsearch()
for project_name_and_value in projects_from_file(fname):
    project_name = project_name_and_value[0]
    project_details = project_name_and_value[1]
    es.index(index="searchmybio_luke", doc_type='project', id=project_name, body=project_details)

