#!/usr/bin/python3
"""
Start a FLASK in a Web Aplication
add a new route: /hbnb
add a new route: /Python
add a new route: /number
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns Hello HBNB!"""
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnh():
    """return HBNB"""
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """Return the letter C"""
    text = text.replace("_", " ")
    return("C {}".format(text))


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def display_Python(text="is cool"):
    """Return the String"""
    text2 = text.replace("_", " ")
    return("Python {}".format(text2))


@app.route('/number/<int:n>', strict_slashes=False)
def Is_Number(n):
    """Return if a parameter is a number"""
    return("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    """Return a HTML PAge if the paramater is a number"""
    return(render_template('5-number.html', number=n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
