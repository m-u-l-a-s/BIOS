from flask import Blueprint, render_template, url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html', lab='imgs/logo_mulas.png')
