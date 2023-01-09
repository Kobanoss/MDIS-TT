from os import getenv


class APP_CONF:
    WS_URL = getenv('WS_URL', 'ws://127.0.0.1:8000/websocket')
    API_URL = getenv('API_URL', 'http://127.0.0.1:5000/api/v1.0/user-contacts')
    PARAMETERS = {
        'SECRET_KEY': getenv('SECRET_KEY_APP', '0eeff27f9c89ab975e01c1eb5aeef5148b1810e9b690a77bedd94a261b3d9b98')}
