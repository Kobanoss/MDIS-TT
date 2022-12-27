from json import dumps
from flask_sock import Sock
from requests import get

from application.routes.__imports__ import *

sock = Sock(App)


@sock.route('/websocket')
def websocket(websock):
    prev_data = None
    while True:
        data = dumps(get(API_URL).json())
        if data != prev_data:
            prev_data = data
            websock.send(data)
