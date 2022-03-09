from flask import Flask, url_for, render_template
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    all = {}
    all["title"] = "тайтл"
    return render_template('index.html', **all)


@app.route("/training/<prof>")
def training(prof):
    all = {}
    all["title"] = "тайтл"
    all["pro"] = prof
    all["first"] = url_for('static', filename='img/rover1.png')
    all["second"] = url_for('static', filename='img/rover2.png')
    return render_template("index.html", **all)


@app.route("/list_prof/<smt>")
def list_prof(smt):
    l = ["строитель", "электрик", "врач", "оператор", "штурман", "пилот", "метеоролог", "экзобиолог"]
    al = {}
    al["l"] = l
    al["smt"] = smt
    return render_template("index.html", **al)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('login.html', title='Авторизация', form=form)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')