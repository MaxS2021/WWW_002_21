from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index1():
    return "Миссия колонизация Марс"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства. </br>

Человечеству мала одна планета.</br>

Мы сделаем обитаемыми безжизненные пока планеты.</br>

И начнем с Марса!</br>

Присоединяйся! """


@app.route('/image_mars')
def image_mars():
    filename = "img/mars-123.jpg"
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename=filename)}" 
                            alt="здесь должна была быть картинка, но не нашлась">'''
                    <h2>Планета Марс.</h2> 
           
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')