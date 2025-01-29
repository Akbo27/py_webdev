from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/te")
def hello_world():
    return "<p>Hello, World from Bo!</p>"

@app.route("/calc/<int:bo>/<int:you>")
def hello_bo(bo,you):
    result = (bo**2) + (you**2)
    return f"<p>{result}</p>"