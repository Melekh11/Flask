from flask import Flask, url_for, render_template
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    all = {}
    all["title"] = "тайтл"
    return render_template('index.html', **all)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('login.html', title='Авторизация', form=form)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')