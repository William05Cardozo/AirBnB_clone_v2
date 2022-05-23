#!/usr/bin/python3
""" 
Write a script that start a FlaskWeb application
Listening on 0.0.0.0 in Port: 5000
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """return a message"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='9000')
  