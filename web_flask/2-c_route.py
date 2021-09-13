#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello1():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hello2():
    return 'HBNB'
# Display "C" followed by the value of the text variable
@app.route('/c/<text>', strict_slashes=False)
    def c_route(text):
    return 'C {}'.format(text.remplace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')