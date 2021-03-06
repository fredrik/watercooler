from mongoengine import Document, EmailField, DateTimeField, ReferenceField, StringField, IntField
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
    name   = StringField(required=True, unique=True)
    weight = IntField(default=0, min_value=0, max_value=10)

class Task(Document):
    raw_text = StringField(required=True)

class Status(Document):
    meta = {
        'indexes': [
            ('user', '-date'),
        ],
    }
    status  = StringField(required=True)
    date    = DateTimeField(default=datetime.utcnow)
    user    = ReferenceField(User, required=True)
    emotion = ReferenceField(Emotion)

    def __json__(self):
        return {
            'status':   self.status,
            'date':     self.date,
            'username': self.user.username,
            'emotion':  self.emotion.name if self.emotion else '',
        }

    def __unicode__(self):
        return "<%s> '%s' at %s" % (self.user.username, self.status, self.date)
