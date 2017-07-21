from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    message = "This is front page"
    return render_template("index.html", message = message)