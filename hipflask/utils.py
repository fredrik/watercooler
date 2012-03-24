import json
from datetime import datetime

def unknown_struct(obj):
    """ Hook called by dumps() when it doesn't know how to
        serialize a struct. It will check if the struc has a __json__
        method defined or if it is a date. Otherwise it will die.
    """
    if hasattr(obj, "__json__"):
        return obj.__json__()
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(repr(obj) + " is not JSON serializable.")

