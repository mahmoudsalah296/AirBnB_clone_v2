#!/usr/bin/python3
"""hbnb routing"""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """hello function"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb function"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def isfun(text):
    """display text from url"""
    return f"C {escape(text).replace('_', ' ')}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", defaults={"text": "is cool"})
def python_route(text):
    """Display 'Python' followed by the value of the text variable)"""
    return f"Python {escape(text.replace('_', ' '))}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
