from flask import Flask, render_template
from flask_jsglue import JSGlue

app = Flask(__name__)
JSGlue(app)

@app.route("/")
def index():
    return render_template("index.html", text = "Hello, world!")