from datetime import datetime
from application.models.__imports__ import *


class UserContacts(Db.Model):
    id = Db.Column(Db.Integer, primary_key=True)
    full_name = Db.Column(Db.String(50), nullable=False)
    birth_date = Db.Column(Db.BigInteger, nullable=False)
    address = Db.Column(Db.String(100), nullable=False)
    phone = Db.Column(Db.BigInteger, nullable=False)
    created_at = Db.Column(Db.DateTime, nullable=False, default=datetime.utcnow)

    def jsonsify(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
