from flask import Flask
from parse import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '1x_parse<br>' \
           '<a href="/h"> /h - Гандбол</a> <br> ' \
           '<a href="/b">/b - Баскетбол</a> <br>'


@app.route('/h')
def h():
    return parse_handball_html()


@app.route('/b')
def b():
    return parse_basket_html()

if __name__ == '__main__':
    app.run()
