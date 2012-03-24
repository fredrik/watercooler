from watercooler.hipflask import app
from models import User, Status
from flask import render_template


@app.route("/")
def hello():
    return render_template('browser.html')


@app.route("/status")
def status():
    """
    Return the latest status for each user.
    """
    statuses = []
    for user in User.objects:
        latest = Status.objects(user=user).first()
        if latest:
            statuses.append(latest)

    return render_template('status.html', statuses=statuses)
