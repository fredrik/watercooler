from watercooler.hipflask.models import Status, User, Emotion, Task
from watercooler.ben.errors import NoSuchUserError
from mongoengine.queryset import DoesNotExist


class Api(object):
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
