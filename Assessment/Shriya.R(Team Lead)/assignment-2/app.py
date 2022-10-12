from unicodedata import name
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/signup")
def sign_up():
    return render_template('signup.html')


@app.route("/signin")
def sign_in():
    return render_template('signin.html')
 
if __name__ == '__main__':
    app.run('0.0.0.0',port = 8080 ,debug=True)
