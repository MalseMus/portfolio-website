from flask import Flask, render_template, request
import requests
import smtplib


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/info')
def info():
    return render_template("info.html")


# Provide name and link
project_dict = {
    "text-to-morse-converter": "https://github.com/MalseMus/text-to-morse-converter",
    "portfolio-website": "Link Soon",
}


@app.route('/projects')
def projects():
    return render_template("projects.html", projects=project_dict)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
