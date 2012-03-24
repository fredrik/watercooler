from watercooler.hipflask import app
from watercooler.hipflask.utils import unknown_struct
from watercooler.ben.api import Api
from models import User, Status
from flask import render_template
from flask import jsonify

import simplejson

from flask.globals import current_app


api = Api()


@app.route("/")
def hello():
    return render_template('browser.html')


@app.route("/api/status/")
def status():
    """
    Return the latest status for each user.
    """
    statuses = api.list_statuses()
    return current_app.response_class(simplejson.dumps(statuses, default=unknown_struct), mimetype='application/json')


@app.route("/api/status/<username>")
def status_for_user(username):
    """
    Return the latest status for one user.
    """
    status = api.get_latest_status(username)
    return current_app.response_class(simplejson.dumps(status, default=unknown_struct), mimetype='application/json')
