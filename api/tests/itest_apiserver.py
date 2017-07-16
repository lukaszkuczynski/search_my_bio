from unittest import TestCase
from api.api_server import app


class ApiServerTest(TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_server_responds_with_hello(self):
        res = self.client.get('/')
        self.assertEquals(res.status_code, 200)

    def test_api_query_endpoint_should_be_return_projects(self):
        endpoint = '/api?q=nodejs'
        response = self.client.get(endpoint)
        print(response)
