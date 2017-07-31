from flask import Flask, render_template, request, jsonify

from config_loader import load_config
from web.dao_elasticsearch import ElasticDao
from web.response_converter import EsResponseConverter

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.debug = True

converter = EsResponseConverter()

elastic_config = load_config('elastic-config.yml')
dao = ElasticDao(elastic_config)


@app.route("/")
def hello():
    message = "This is front page"
    return render_template("index.html", message = message)


@app.route("/cv")
def cv():
    response = dao.docs_sorted_by_date(innertype='commercial')
    commercial_projects = response['hits']['hits']
    response = dao.docs_sorted_by_date(innertype='private')
    private_projects = response['hits']['hits']
    context = {
        'commercial_projects' : commercial_projects,
        'private_projects': private_projects
    }
    return render_template("static_cv.html", context = context)

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/api/search")
def api_search():
    queried_text = request.args.get("q")
    if queried_text == '':
        queried_text = '*'
    print('query is %s' % queried_text)
    response = dao.query_all_fields(queried_text)
    simple_response = converter.response_to_simple_hits(response)
    return jsonify(simple_response)

@app.route("/api/all")
def all():
    print("returning all docs")
    response = dao.all_docs_sorted_by_date()
    simple_response = converter.response_to_simple_hits(response)
    return jsonify(simple_response)

if __name__ == '__main__':
    app.run()