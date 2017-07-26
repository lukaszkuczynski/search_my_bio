from api.response_converter import EsResponseConverter
from unittest import TestCase


class ResponseConverterTest(TestCase):

    def test_response_should_be_converted(self):
        converter = EsResponseConverter()
        response = {
                "took": 4,
                "timed_out": False,
                "_shards": {
                    "total": 5,
                    "successful": 5,
                    "failed": 0
                },
                "hits": {
                    "total": 1,
                    "max_score": 0.35870585,
                    "hits": [
                        {
                            "_index": "searchmybio_luke",
                            "_type": "project",
                            "_id": "Mini REST service for my CD Collection",
                            "_score": 0.35870585,
                            "_source": {
                                "started at": "2013-02",
                                "tasks": [
                                    "care about whole app"
                                ],
                                "learned": [
                                    "NodeJS + Express = fast web or Rest app written in JS!"
                                ],
                                "challenges": [
                                    "which library on npm to choose?!"
                                ],
                                "technologies": [
                                    "NodeJS",
                                    "Express",
                                    "javascript"
                                ],
                                "measure of success": [
                                    "REST app in 6 days"
                                ]
                            }
                        }
                    ]
                }
        }
        converted = converter.response_to_simple_hits(response)
        self.assertEquals(converted[0]["score"], 0.35870585)
        self.assertEquals(converted[0]["source"]["started at"], "2013-02")
        self.assertEquals(converted[0]["id"], "Mini REST service for my CD Collection")