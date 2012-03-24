from flask import Flask
app = Flask(__name__)
app.config.from_object('watercooler.hipflask.config.Configuration')

# views.
# "all the view functions (the ones with a route() decorator on top)
# have to be imported when in the __init__.py file. Not the object
# itself, but the module it is in. Import the view module after the
# application object is created."
# http://flask.pocoo.org/docs/patterns/packages/#simple-packages
import watercooler.hipflask.views
