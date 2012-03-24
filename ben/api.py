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
    def add_status(self, status, user, emotion_or_emotionname=None):

        if not type(user) == User:
            # convert to User object
            username = user
            try:
                user = User.objects.get(username=username)
            except DoesNotExist:
                raise NoSuchUserError()

        if emotion_or_emotionname and not type(emotion_or_emotionname) == Emotion:
            # convert to Emotion object
            try:
                emotion = Emotion.objects.get(name=emotion_or_emotionname)
            except DoesNotExist:
                emotion = Emotion(name=emotion_or_emotionname)
                emotion.save()
        else:
            emotion = emotion_or_emotionname

        # save status.
        Status(status=status, user=user, emotion=emotion).save()
