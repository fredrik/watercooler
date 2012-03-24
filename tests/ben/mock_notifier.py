class MockNotifier(object):
    notifications = []
    def notify(self, username):
        self.notifications.append({'username': username})
