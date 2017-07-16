class EsResponseConverter:

    def response_to_simple_hits(self, response):
        simple_hits = [{"score": hit['_score'], "source": hit['_source']} for hit in response['hits']['hits']]
        return simple_hits
