from mongoengine import Document
from mongoengine.fields import StringField, IntField


class UserModel(Document):
    username = StringField()
    age = IntField()
    meta = {'db_alias': 'user-db'}