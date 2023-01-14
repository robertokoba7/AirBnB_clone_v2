#!/usr/bin/python3
"""what the program does"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    text = text.replace('_', " ")
    """Returns C is fun!"""
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Returns python is magic and also 'is cool' by default"""
    if text != 'is cool':
        text = text.replace('_', " ")
    """Returns python is magic with default text "is cool"!"""
    return 'python {}'.format(text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
