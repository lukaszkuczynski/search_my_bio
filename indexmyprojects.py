import yaml
from elasticsearch import Elasticsearch

from config_loader import load_config

def projects_from_file(fname):
    with open(fname) as f:
        doc = yaml.load(f)
        commercial = doc['Projects']['Commercial']
        for project in commercial.keys():
            yield ('commercial', project, commercial[project])
        private = doc['Projects']['Private']
        for project in private.keys():
            yield ('private', project, private[project])


if __name__ == '__main__':

    fname = "life_tasks.yml"

    elastic_hosts = load_config('elastic-config.yml')
    es = Elasticsearch(hosts=elastic_hosts, verify_certs=False)
    for project_tuple in projects_from_file(fname):
        commercial_or_private = project_tuple[0]
        project_name = project_tuple[1]
        project_details = project_tuple[2]
        project_details['title'] = project_name
        project_details['type'] = commercial_or_private
        es.index(index="searchmybio_luke", doc_type='project', id=project_name, body=project_details)


