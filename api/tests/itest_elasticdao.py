from api.dao import ElasticDao
from unittest import TestCase

class IntegrationTestElasticDao(TestCase):

    def setUp(self):
        self.dao = ElasticDao()

    def test_elastic_hello(self):
        hello = self.dao.hello()
        self.assertIsNotNone(hello)
