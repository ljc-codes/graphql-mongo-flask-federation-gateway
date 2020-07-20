from mongoengine import Document
from mongoengine.fields import StringField, ReferenceField

from .UserModel import UserModel


class ReviewModel(Document):
    name = StringField()
    user = ReferenceField(UserModel)
    meta = {'db_alias': 'review-db'}