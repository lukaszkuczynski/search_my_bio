from elasticsearch import Elasticsearch

es = Elasticsearch()


es.indices.delete("searchmybio_luke")
print("Creating index")
res = es.indices.create("searchmybio_luke")
print("Result %s" % res)
