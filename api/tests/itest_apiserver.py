from unittest import TestCase
from api.api_server import app


class ApiServerTest(TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_server_responds_with_hello(self):
        res = self.client.get('/')
        self.assertEquals(res.status_code, 200)
