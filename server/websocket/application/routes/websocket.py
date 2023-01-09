from json import dumps
from flask_sock import Sock, Server
from requests import get

from application.routes.__imports__ import *

sock = Sock(App)


@sock.route('/websocket')
def websocket(websock: Server):
    prev_data = None
    while True:
        data_j = get(API_URL).json()
        data = dumps(data_j)
        if len(data_j.keys()) < 2:
            continue
        if data != prev_data:
            prev_data = data
            websock.send(data)
