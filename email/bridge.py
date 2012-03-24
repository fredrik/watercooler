import os
os.environ['WATERCOOLER_ENVIRONMENT'] = 'test'

from watercooler.hipflask import environment
from watercooler.hipflask.models import User
from mongoengine.queryset import DoesNotExist
#from watercooler.ben.api import Api
#from watercooler.email import either pull or pushed emails.

asd = [
    {'email':'test@testing.com', 'from': 'Simon Johansson', 'message': "I'm feeling happy\nI'm working on stuff"}
]

def get_user(email):
    email_addr = email.get('email')
    try:
        return User.objects.get(email=email.get('email'))
    except DoesNotExist:
        print "A user for %s doesnt exist, adding it!" % email_addr
        username = email_addr.split('@')[0]
        first_name, last_name = email.get('from').split() # People with more than one name can bugger of.
        user = User(first_name=first_name, last_name=last_name, email=email.get('email'), username=username)
        user.save()
        return user

def bridge():
    for email in asd:# <- get_emails()
        user = get_user(email)
        email_message = email.get('message')
        #Api.new_email(email=email_message, user=user) <- or something similar?
        
if __name__ == '__main__':
    bridge()
