from flask import Flask
from application.config import APP_CONF

App = Flask(__name__)
for param, value in APP_CONF.PARAMETERS.items():
    App.config[param] = value

API_URL = APP_CONF.API_URL

from application.routes import sock
