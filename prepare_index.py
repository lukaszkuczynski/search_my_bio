from elasticsearch import Elasticsearch

es = Elasticsearch()

print("Creating index")
res = es.indices.create("searchmybio_luke")
print("Result %s" % res)
