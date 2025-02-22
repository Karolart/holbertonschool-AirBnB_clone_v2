#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def task_0():
    """
    Function that returns and display
    “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def task_1():
    """
    Function that returns and display
    “HBNB”
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def task_2(text):
    """
    Function that recieves route args and
    returns 'C {text}'
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False, defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def task_3(text):
    """
    Function that recieves route args and
    returns 'Python {text}' as previous function
    but has 'is cool' as default
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def task_4(n):
    """
    Function that recieves an integer as route args
    and return '{n} is a number'
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def task_5(n):
    """
    Function that return a template renderized
    and passed args
    """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def task_6(n):
    """
    Function that return a template renderized
    and passed args and check if it's
    an odd or even number
    """
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
