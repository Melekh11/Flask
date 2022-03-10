from flask import Flask, url_for, render_template
# from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# a = url_for('static', filename='img/scale_1200.jpeg')
# print(a)


@app.route('/index/<tit>')
def index(tit):
    all = {}
    all["title"] = tit
    return render_template('index.html', **all)


@app.route("/")
@app.route("/training/<prof>")
def training(prof):
    all = {}
    all["prof"] = prof
    all["link1"] = url_for('static', filename='img/rover1.png')
    all["link2"] = url_for('static', filename='img/rover2.png')
    print("!!!!!!!")
    print(url_for('static', filename='img/scale_1200.jpeg'))
    return render_template("index.html", **all)





# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('login.html', title='Авторизация', form=form)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')