from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'thisismysecretkeydonotstealit'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    db.init_app(app)

    #login_manager = LoginManager()
    #login_manager.login_view = 'auth.login'
    #login_manager.init_apfrom flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    # Flask Object
    app = Flask(__name__)
    app.config['SECRET_KEY'] = random._urandom(56)
    app.config['DEBUG'] = True
    #Bootstrap(app)

    # Database Connection
    #db_info = {'host': 'localhost',
    #          'database': 'bookstore',
    #         'psw': '1234',
    ##       'port': ''}
    #app.config[
    #   'SQLALCHEMY_DATABASE_URI'] = f"postgres://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    import os
    basedir = os.path.abspath(os.path.dirname(__file__)) # Try to avoid hardcoding paths, use os

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'app.db')
    # This line is adding sqlite:/// with the path of your database

    # Database Representation
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)


    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return appp(app)

    #from .models import User

    #@login_manager.user_loader
    #def load_user(user_id):
        #return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #return app