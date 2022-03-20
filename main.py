import json

from flask import Flask, url_for, request, render_template, redirect
from PIL import Image
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


arr_names = ["Паша", "Саша", "Маша", "Петя", "Игорёк", "Васечка", "Анечка"]

@app.route("/answer")
@app.route("/auto_answer")
def ans():
    all= {}
    with open("ans.json", "r", encoding="utf-8") as file:
        all["ans"] = json.load(file)
    return render_template("index.html", **all)


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/success")
def success():
    return "success"


@app.route("/distribution")
def distribution():
    all = {}
    all["pass"] = arr_names
    return render_template("index.html", **all)


@app.route("/table/<string:who>/<int:age>")
def table(who, age):
    all={}
    all["who"] = who
    all["age"] = age
    return render_template("table.html", **all)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')