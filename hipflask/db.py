# connect to mongo
from mongoengine import connect
from watercooler.hipflask import environment

database_name = 'watercooler-' + environment.ENVIRONMENT
connect(database_name)
