from unittest import TestCase
from api.api_server import app
import json


class ApiServerTest(TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_server_responds_with_hello(self):
        res = self.client.get('/')
        self.assertEquals(res.status_code, 200)

    def test_api_query_endpoint_should_be_return_projects(self):
        endpoint = '/api/search?q=nodejs'
        response = self.client.get(endpoint)
        self.assertEquals(response.status_code, 200)
        text = response.data
        json_reponse = json.loads(text)
        self.assertEquals(len(json_reponse), 1)
        self.assertEquals(json_reponse[0]['score'], 0.35870585)
