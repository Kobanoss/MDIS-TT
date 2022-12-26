from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from application.config import APP_CONF

App = Flask(__name__)
for param, value in APP_CONF.PARAMETERS.items():
    App.config[param] = value

Db = SQLAlchemy(App)

from application.routes import api
from application.models.user_model import UserContacts

App.register_blueprint(api, url_prefix='/')

with App.app_context():
    Db.create_all()
    Db.session.commit()
