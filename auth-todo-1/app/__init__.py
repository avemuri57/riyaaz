from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from config import app_config

CONFIG_PYFILE = 'config.py'

login_manager = LoginManager()
db = SQLAlchemy()
LOGIN_MESSAGE = "You Are Unauthorized to View This Page"
LOGIN_VIEW = "auth.login"
csrf = CSRFProtect()

def create_app(config_name):
	app = Flask(__name__,instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile(CONFIG_PYFILE)


	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	from .home import home as home_blueprint
	app.register_blueprint(home_blueprint)
	
	login_manager.init_app(app)
	login_manager.login_message = LOGIN_MESSAGE
	login_manager.login_view = LOGIN_VIEW

	db.init_app(app)
	csrf.init_app(app)
	migrate = Migrate(app,db)
	
	from app import models

	return app
