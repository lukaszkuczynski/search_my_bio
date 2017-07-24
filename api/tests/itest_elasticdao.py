from api.dao_elasticsearch import ElasticDao
from unittest import TestCase

class IntegrationTestElasticDao(TestCase):

    def setUp(self):
        config = {
            "host": "localhost",
            "port": 9200,
            "index_pattern": "searchmybio_luke"
        }
        self.dao = ElasticDao(config)

    def test_elastic_is_alive(self):
        alive = self.dao.is_alive()
        self.assertTrue(alive)

    def test_cluster_contains_index(self):
        index_is_present = self.dao.is_index_present()
        self.assertTrue(index_is_present)

    def test_cluster_is_configured(self):
        configured = self.dao.is_cluster_configured()
        self.assertTrue(configured)

    def test_dao_matches_text(self):
        response = self.dao.query_all_fields("nodejs")
        self.assertIs(len(response['hits']['hits']), 1)

    def test_dao_returns_all_docs(self):
        response = self.dao.all_docs_sorted_by_date()
        hits = response['hits']['hits']
        if len(hits) > 1:
            first_date = hits[0]['_source']['started']
            last_date = hits[len(hits)-1]['_source']['started']
            self.assertGreater(first_date, last_date)
