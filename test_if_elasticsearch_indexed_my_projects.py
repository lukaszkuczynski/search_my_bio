from unittest import TestCase
from elasticsearch import Elasticsearch

class TestElasticsearchIndexing(TestCase):

    def setUp(self):
        self.es = Elasticsearch()

    def test_index_is_searchable(self):
        query_find_nodejs = {
            "query": {
                "match": {
                    "technologies": "nodejs"
                }
            }
        }
        res = self.es.search(index='searchmybio_luke', doc_type='project', body=query_find_nodejs)
        hits = res['hits']['hits']
        self.assertEquals(len(hits), 1)
