from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_restful import Resource, Api #
from flask_jwt import JWT, jwt_required #
import os

basedir = os.path.abspath(os.path.dirname(__file__))
#from website.security import authenticate, identity #

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'website.db')
app.config['SECRET_KEY'] = 'hard to guess string'
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
db.app = app
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)
@app.before_first_request
def create_tables():
    from website.models import User
    db.create_all()

login.login_view = 'login'

#app.secret_key = 'jose' #
#api = Api(app) #
#jwt = JWT(app, authenticate, identity) # /auth

from website import routes, models