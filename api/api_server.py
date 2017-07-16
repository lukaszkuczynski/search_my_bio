from flask import Flask, request, jsonify
from api.dao_elasticsearch import ElasticDao
from api.response_converter import EsResponseConverter

app = Flask(__name__)
converter = EsResponseConverter()

elastic_config = {
    "host": "localhost",
    "port": 9200
}
dao = ElasticDao(elastic_config)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/search")
def api_search():
    queried_text = request.args.get("q")
    response = dao.query_all_fields(queried_text)
    simple_response = converter.response_to_simple_hits(response)
    return jsonify(simple_response)
