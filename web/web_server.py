from flask import Flask, render_template, request, jsonify
import datetime, logging
from logging import handlers


from config_loader import load_config
from web.dao_elasticsearch import ElasticDao

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.debug = True

LOG_FILENAME = 'app_access_logs.log'

app.logger.setLevel(logging.INFO) # use the native logger of flask

handler = handlers.RotatingFileHandler(
    LOG_FILENAME,
    maxBytes=1024 * 1024 * 100,
    backupCount=20
    )

app.logger.addHandler(handler)

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
    return jsonify(response)

if __name__ == '__main__':
    app.run()

@app.before_request
def pre_request_logging():
    #Logging statement
    # if 'text/html' in request.headers['Accept']:
    app.logger.info('\t'.join([
        datetime.datetime.today().ctime(),
        request.remote_addr,
        request.method,
        request.url,
        # str(request.data,
        # ', '.join([': '.join(x) for x in request.headers])]
        ])
    )