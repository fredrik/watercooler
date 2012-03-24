from mongoengine import Document, EmailField, DateTimeField, ReferenceField
from datetime import datetime


class User(Document):
    meta = {
        'indexes': [
            'username',
        ]
    }
    first_name = StringField(required=True)
    last_name  = StringField(required=True)
    email      = EmailField(required=True, unique=True)
    username   = StringField(required=True, unique=True) # extracted from email.


# happy, sad.
class Emotion(Document):
    name   = StringField(required=True)
    weight = IntField(default=0, min_value=0, max_value=10)

class Task(Document):
    raw_text = StringField(required=True)

class Status(Document):
    meta = {
        'indexes': [
            ('user', '-date'),
        ]
    }
    date    = DateTimeField(default=datetime.utcnow)
    user    = ReferenceField(User)
    emotion = ReferenceField(Emotion)
