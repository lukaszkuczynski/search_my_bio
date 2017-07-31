from web.dao_elasticsearch import ElasticDao
from unittest import TestCase
from config_loader import load_config

class IntegrationTestElasticDao(TestCase):

    def setUp(self):
        config = load_config("elastic-config.yml")
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

    def test_dao_returns_docs_by_type(self):
        response = self.dao.docs_sorted_by_date(innertype='commercial')
        hits = response['hits']['hits']
        self.assertTrue(len(hits) > 0)
        if len(hits) > 1:
            first_type = hits[0]['_source']['type']
            self.assertEquals("commercial", first_type)
        response = self.dao.docs_sorted_by_date(innertype='private')
        hits = response['hits']['hits']
        self.assertTrue(len(hits) > 0)
        if len(hits) > 1:
            first_type = hits[0]['_source']['type']
            self.assertEquals("private", first_type)
