from os import getenv


class APP_CONF:
    PARAMETERS = {
        'SECRET_KEY': getenv('SECRET_KEY', '0eeff27f9c89ab975e01c1eb5aeef5148b1810e9b690a77bedd94a261b3d9b98'),
        'SQLALCHEMY_DATABASE_URI': f'{getenv("DATABASE_URL", "sqlite:///test.sqlite")}',
        'SQLALCHEMY_TRACK_MODIFICATIONS': True}
