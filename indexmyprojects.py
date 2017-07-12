import yaml
from elasticsearch import Elasticsearch

fname = "projects.yml"
with open(fname) as f:
    doc = yaml.load(f)
    commercial = doc['Projects']['Commercial']
    print("--Listing commercial projects--")
    for project in commercial.keys():
        print(project)
    private = doc['Projects']['Private']
    print("--Listing side-projects--")
    for project in private.keys():
        print(project)

es = Elasticsearch()
print(es.info())