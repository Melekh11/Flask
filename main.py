# c днём рождения Вас!!)

from flask import Flask, url_for, request
from PIL import Image

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def image_mars():
    if request.method == 'POST':
        f = request.files['file']
        f.save("static/img/pic.png")
        im = Image.open("static/img/pic.png")
        im2 = im.resize((430, 430))
        im2.save('static/img/pic.png')

        return f'''<!doctype html>
                                        <html lang="en">
                                          <head>
                                            <meta charset="utf-8">
                                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                            <link rel="stylesheet"
                                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                            crossorigin="anonymous">
                                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                            <title>Пример формы</title>
                                          </head>
                                          <body>
                                            <div>
                                                <form class="login_form" method="post" enctype="multipart/form-data">
                                                    <label>Загрузите Ваше фото</label>
                                                    <div class="form-group">
                                                        <label for="photo">Приложите фотографию</label>
                                                        <input type="file" class="form-control-file" id="photo" name="file">
                                                    </div>   
                                                    <img src="{url_for('static', filename='img/pic.png')}"
                                                        alt="здесь должна была быть картинка, но не нашлась">
                                                     <button type="submit" class="btn btn-primary">Показать</button>
                                                </form>
                                            </div>
                                          </body>
                                        </html>'''
    elif request.method == 'GET':
        return f'''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet"
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                    crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                    <title>Пример формы</title>
                                  </head>
                                  <body>
                                    <div>
                                        <form class="login_form" method="post" enctype="multipart/form-data">
                                            <label>Загрузите Ваше фото</label>
                                            <div class="form-group">
                                                <label for="photo">Приложите фотографию</label>
                                                <input type="file" class="form-control-file" id="photo" name="file">
                                            </div>   
                                             <button type="submit" class="btn btn-primary">Показать</button>
                                        </form>
                                    </div>
                                  </body>
                                </html>'''



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')