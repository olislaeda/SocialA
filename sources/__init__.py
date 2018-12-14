from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

sa = Flask(__name__)
sa.config.from_object(Config)
db = SQLAlchemy(sa)
lm = LoginManager(sa)
lm.login_view = 'login'

migrate = Migrate(sa, db)
from sources import destinations
from sources.dbstruct import users, posts