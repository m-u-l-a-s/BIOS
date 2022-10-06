from flask import Flask, render_template, url_for, redirect, request

lab = '../static/imgs/lab302.png'
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", lab = lab)

@app.route("/consulta")
def consulta():
    return render_template("consulta.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        lab = request.form.get("lab")
        if (lab >= "301") and (lab <= "309"):
            lab = '../static/imgs/Lab302.png'
        else:
            lab = '../static/imgs/Lab402.png'
    return render_template("index.html", lab=lab,)

