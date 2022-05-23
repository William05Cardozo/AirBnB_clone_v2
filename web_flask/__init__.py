#!/usr/bin/python3

""" 
Write a script that start a FlaskWeb application
Listening on 0.0.0.0 in Port: 5000
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', stric_slasher=False)
def hello_HNBN():
    # Return a message
    return "Hello HBNB!"

if __name__ == "__main":
    # Your web application must be listening on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)