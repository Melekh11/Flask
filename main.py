from flask import Flask, url_for, request,render_template
from PIL import Image

app = Flask(__name__)


@app.route('/')
def image_mars():
    return render_template("index1.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')