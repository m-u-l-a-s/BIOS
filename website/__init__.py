from flask import Flask, render_template, url_for
from .database import create_oss_table, create_users_table, create_database

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

    try: create_database()
    except: pass
    try: create_oss_table()
    except: pass
    try: create_users_table()
    except: pass


    return app

