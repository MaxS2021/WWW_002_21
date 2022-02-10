from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index1():
    return "Миссия колонизация Марс"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')