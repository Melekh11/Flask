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
                                        <title>Привет, Яндекс!</title>
                                      </head>
                                      <body>
                                        <img src="{url_for('static', filename='img/scale_1200.jpeg')}"
                                           alt="здесь должна была быть картинка, но не нашлась">
                                           <p>красиво...</p>
                                      </body>
                                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')