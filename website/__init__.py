from flask import Flask, render_template, url_for
# Este arquivo transforma a pasta "site" em um módulo.
# Com isso, qualquer função criada por um arquivo .py
# pode ser importada.

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mulas'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

