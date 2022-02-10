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
    filename = "img/mars1.jpg"
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


@app.route('/promotion_image')
def promotion_image():
    filename = "img/mars1.jpg"
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename=filename)}" 
                                alt="здесь должна была быть картинка, но не нашлась">'''
                        <h2>Планета Марс.</h2> 
                        <div class="alert alert-primary" role="alert">
                            Человечество вырастет когда-нибудь, наверное, мы надеемся очень, из детства!
                        </div>
                        <div class="alert alert-success" role="alert">
                            Человечеству мало одной планеты!
                        </div>
                        <div class="alert alert-danger" role="alert">
                            Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                            И начнем с Марса!
                        </div>
                      </body>
                    </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')