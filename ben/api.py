from watercooler.hipflask.models import Status, User, Emotion, Task

class Api(object):
    """
    Add status for a user.

    +status+ is a string. Required.
    +user+ is a User object or a username. Required.
    +emotion+ is an Emotion object or an emotionname. Optional.
    """
    def add_status(self, status, user, emotion=None):
        Status(status=status, user=user, emotion=emotion).save()
