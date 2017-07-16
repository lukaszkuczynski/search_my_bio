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