#!/usr/bin/python3
"""hbnb routing"""

from flask import Flask, render_template
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
@app.route("/python", strict_slashes=False, defaults={"text": "is cool"})
def python_route(text):
    """Display 'Python' followed by the value of the text variable)"""
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """display 'n is a number' only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_temp_route(n):
    """display html page only if n is an integer"""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    """display even or odd html page only if n is an integer"""
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
