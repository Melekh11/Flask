import json

from flask import Flask, url_for, request,render_template
from PIL import Image

app = Flask(__name__)


@app.route('/')
def image_mars():
    return render_template("index.html")


@app.route("/answer")
@app.route("/auto_answer")
def ans():
    all= {}
    with open("ans.json", "r", encoding="utf-8") as file:
        all["ans"] = json.load(file)
    return render_template("index.html", **all)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')