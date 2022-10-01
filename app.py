from flask import Flask, render_template

app = Flask(__name__)

title = "Heric"

@app.route("/")
def home():
    return render_template("index.html", title=title)

@app.route("/consulta")
def consulta():
    return render_template("consulta.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/index")
def index():
    return render_template("index.html")
