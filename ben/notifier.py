import os
import requests

class NodeNotifier(object):
    def __init__(self, remote_address='http://localhost:6600'):
        self.remote_address = remote_address
    def notify(self, username):
        """
        Send a notification signaling that this user has a new status.
        """
        path    = 'new_status'
        url     = os.path.join(self.remote_address, path)
        data    = {'username': username}

        response = requests.post(url, data)
