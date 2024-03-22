#!/usr/bin/python3
"""run the flask """
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return ("Hello HBNB!")

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return ("HBNB")

@app.route("/c/<string>", strict_slashes=False)
def c_is(string):
    if string:
        new = string.replace("_", " ")
        return (f"C {new}")
@app.route("/python", strict_slashes=False)
@app.route("/python/<string>", strict_slashes=False)
def Python_is(string="is cool"):
    new = string.replace("_", " ")
    return (f"Python {new}")

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return (f"{n} is a number")

@app.route("/number_template/<int:n>", strict_slashes=False)
def ren_html(n):
    return (render_template("5-number.html", n=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
