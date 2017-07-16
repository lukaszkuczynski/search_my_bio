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