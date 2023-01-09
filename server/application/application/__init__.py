from flask import Flask
from application.config import APP_CONF

App = Flask(__name__, template_folder='./templates', static_folder='./static')
for param, value in APP_CONF.PARAMETERS.items():
    App.config[param] = value

API_URL = APP_CONF.API_URL
WS_URL = APP_CONF.WS_URL

from application.routes import views

App.register_blueprint(views, url_prefix='/')
