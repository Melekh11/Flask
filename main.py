from flask import Flask, url_for

app = Flask(__name__)


@app.route('/index')
def index1():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route("/promotion")
def promotion():
    return "<h2>Человечество вырастает из детства.</h2>" \
           "<h2>Человечеству мала одна планета.</h2>" \
           "<h2>Мы сделаем обитаемыми безжизненные пока планеты.</h2>" \
           "<h2>И начнем с Марса!</h2>" \
           "<h2>Присоединяйся!</h2>"


@app.route("/")
def image_mars():
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

                            <h1 class="login_form">Форма для регистрации в суперсекретной системе</h1>

                            <div>
                                <form class="login_form" method="post">
                                    <input type="name" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Введите имя" name="name">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="email" class="form-control" id="email" placeholder="Введите почту" name="email">

                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>


                                    <label>Какие у Вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <div>
                                        <label for="acceptRules">инженер-исследователь</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        </div>
                                        
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules1">пилот</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules1" name="accept1">
                                        </div>
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules13">строитель</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules13" name="accept2">
                                        </div>
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules2">экзобиолог</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules2" name="accept3">
                                        </div>
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules3">врач</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules3" name="accept4">
                                        </div>
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules4">инженер по терраформированию</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules4" name="accept5">
                                        </div>
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules5">климатолог</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules5" name="accept6">
                                        </div>
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules6">специалист по радиационной защите</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules6" name="accept7">
                                        </div>
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules15">астрогеолог</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules15" name="accept8">
                                        </div>
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules7">гляциолог</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules7" name="accept9">
                                        </div>
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules8">инженер жизнеобеспечения</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules8" name="accept10">
                                        </div>
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules9">метеоролог</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules9" name="accept11">
                                        </div>
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules10">оператор марсохода</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules10" name="accept12">
                                        </div>
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules11">киберинженер</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules11" name="accept13">
                                        </div>
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules12">штурман</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules12" name="accept14">
                                        </div>
                                        
                                        <div>
                                        <label class="form-check-label" for="acceptRules13">пилот дронов</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules13" name="accept15">
                                        </div>
                                        
                                    </div>

                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участия в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>

                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>

                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>

                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

    # < label
    #
    #
    # class ="form-check-label" for ="acceptRules2" > экзобиолог < / label >
    #
    # < input
    # type = "checkbox"
    #
    #
    # class ="form-check-input" id="acceptRules2" name="acceptRules2" >
    #
    # < label
    #
    #
    # class ="form-check-label" for ="acceptRules3" > врач < / label >
    #
    # < input
    # type = "checkbox"
    #
    #
    # class ="form-check-input" id="acceptRules3" name="acceptRules3" >
    #
    # < label
    #
    #
    # class ="form-check-label" for ="acceptRules4" > инженер по терраформированию < / label >
    #
    # < input
    # type = "checkbox"
    #
    #
    # class ="form-check-input" id="acceptRules4" name="acceptRules4" >
    #
    # < label
    #
    #
    # class ="form-check-label" for ="acceptRules5" > климатолог < / label >
    #
    # < input
    # type = "checkbox"
    #
    #
    # class ="form-check-input" id="acceptRules5" name="acceptRules5" >
    #
    # < label
    #
    #
    # class ="form-check-label" for ="acceptRules6" > специалист по радиационной защите < / label >
    #
    # < input
    # type = "checkbox"
    #
    #
    # class ="form-check-input" id="acceptRules6" name="acceptRules6" >
    #
    # < label
    #
    #
    # class ="form-check-label" for ="acceptRules15" > астрогеолог < / label >
    #
    # < input
    # type = "checkbox"
    #
    #
    # class ="form-check-input" id="acceptRules15" name="acceptRules15" >
    #
    # < label
    #
    #
    # class ="form-check-label" for ="acceptRules7" > гляциолог < / label >
    #
    # < input
    # type = "checkbox"
    #
    #
    # class ="form-check-input" id="acceptRules7" name="acceptRules7" >
    #
    # < label
    #
    #
    # class ="form-check-label" for ="acceptRules8" > инженер жизнеобеспечения < / label >
    #
    # < input
    # type = "checkbox"
    #
    #
    # class ="form-check-input" id="acceptRules8" name="acceptRules8" >
    #
    # < label
    #
    #
    # class ="form-check-label" for ="acceptRules9" > метеоролог < / label >
    #
    # < input
    # type = "checkbox"
    #
    #
    # class ="form-check-input" id="acceptRules9" name="acceptRules9" >
    #
    # < label
    #
    #
    # class ="form-check-label" for ="acceptRules10" > оператор марсохода < / label >
    #
    # < input
    # type = "checkbox"
    #
    #
    # class ="form-check-input" id="acceptRules10" name="acceptRules10" >
    #
    # < label
    #
    #
    # class ="form-check-label" for ="acceptRules11" > штурман < / label >
    #
    # < input
    # type = "checkbox"
    #
    #
    # class ="form-check-input" id="acceptRules11" name="acceptRules11" >
    #
    # < label
    #
    #
    # class ="form-check-label" for ="acceptRules13" > пилот дронов < / label >
    #
    # < input
    # type = "checkbox"
    #
    #
    # class ="form-check-input" id="acceptRules13" name="acceptRules13" >