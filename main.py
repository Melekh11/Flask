# c днём рождения Вас!!)

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/index')
def index1():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route("/promotion")
def promotion():
    return"<h2>Человечество вырастает из детства.</h2>" \
          "<h2>Человечеству мала одна планета.</h2>" \
          "<h2>Мы сделаем обитаемыми безжизненные пока планеты.</h2>" \
          "<h2>И начнем с Марса!</h2>" \
          "<h2>Присоединяйся!</h2>"


@app.route("/image_mars")
def image_mars():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Колонизация</title>
                          </head>
                          <body>
                            <h1 class="login_form">Жди нас, Марс</h1>
                            <img src="{url_for('static', filename='img/scale_1200.jpeg')}"
                                alt="здесь должна была быть картинка, но не нашлась">
                            <div class="alert alert-primary" role="alert">
                              Когда человек изобретёт фотонный двигатель
                            </div>
                            <div class="alert alert-secondary" role="alert">
                              вообще круто будет
                            </div>
                            <div class="alert alert-success" role="alert">
                              ну а пока
                            </div>
                            <div class="alert alert-danger" role="alert">
                              пишем рекламки планет
                            </div>
                            <div class="alert alert-warning" role="alert">
                              такие дела
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
