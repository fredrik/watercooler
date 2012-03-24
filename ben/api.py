from watercooler.hipflask.models import Status, User, Emotion, Task
from watercooler.ben.notifier import NodeNotifier
from watercooler.ben.errors import NoSuchUserError
from mongoengine.queryset import DoesNotExist


class Api(object):

    def __init__(self, notifier=NodeNotifier()):
        self.notifier = notifier

    """
    Add status for a user.

    +status+ is a string. Required.
    +user+ is a User object or a username. Required.
    +emotion+ is an Emotion object or an emotionname. Optional.
    """
    def add_status(self, status, user, emotion=None):

        if not type(user) == User:
            # convert to User object
            username = user
            try:
                user = User.objects.get(username=username)
            except DoesNotExist:
                raise NoSuchUserError()

        if emotion and not type(emotion) == Emotion:
            # convert to Emotion object
            emotionname = emotion
            try:
                emotion = Emotion.objects.get(name=emotionname)
            except DoesNotExist:
                emotion = Emotion(name=emotionname)
                emotion.save()

        # save status.
        Status(status=status, user=user, emotion=emotion).save()
        self.notifier.notify(user.username)


    """
    List the most recent status for each user, sorted by date posted.
    """
    def list_statuses(self):
        statuses = []
        for user in User.objects:
            latest = Status.objects(user=user).order_by('-date').first()
            if latest:
                statuses.append((latest.date, latest))
        # order by date
        return [status for date,status in sorted(statuses, reverse=True)]
