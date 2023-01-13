#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Returns a text to the client
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns HBNB to the client
    """
    return "HBNB"


if __name__ == '__main__':
    """
    Runs when this script is not imported
    """
    app.run(host="0.0.0.0", port=5000)
