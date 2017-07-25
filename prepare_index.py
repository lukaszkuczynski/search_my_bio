from elasticsearch import Elasticsearch

es = Elasticsearch()

print("Removing index")
es.indices.delete("searchmybio_luke", ignore=[400, 404])
print("Creating index and type with mapping")
mapping = {
    "mappings": {
        "projects": {
            "properties": {
                "started": {
                    "type": "date",
                    "format": "yyyy-MM"
                },
                "finished": {
                    "type": "date",
                    "format": "yyyy-MM"
                }

            }
        }
    }
}

res = es.indices.create("searchmybio_luke", body=mapping)
print("Result %s" % res)
