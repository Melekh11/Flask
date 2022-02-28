# c днём рождения Вас!!)

from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Привет, колонизатор</h1>"


@app.route('/choice/<planet_name>')
def image_mars(planet_name):
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <title>Выбор планеты</title>
                          </head>
                          <body>
                            <div class="alert alert-primary" role="alert">
                              <h1>моя рекомендация: {planet_name}</h1>
                            </div>
                            <div class="alert alert-secondary" role="alert">
                              <h2>планета крутая</h2>
                            </div>
                            <div class="alert alert-success" role="alert">
                              <h3>с виду кгруглая</h3>
                            </div>
                            <div class="alert alert-danger" role="alert">
                              <h4>что ещё надо</h4>
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')