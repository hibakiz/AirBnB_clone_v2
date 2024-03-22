#!/usr/bin/python3
"""run the flask """
from flask import Flask
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
