from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/search')
def search(user_str):
    tweets = request.args.get()

    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run(use_reloader=True)