from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.debug = True

@app.route("/")
def hello():
    message = "This is front page"
    return render_template("index.html", message = message)


@app.route("/cv")
def cv():
    return render_template("static_cv.html")