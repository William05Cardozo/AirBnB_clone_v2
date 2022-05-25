#!/usr/bin/python3

from flask import *
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def flask_0():
    return(“Hello HBNB!”)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500i0, debug=True)
