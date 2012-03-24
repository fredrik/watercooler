import unittest2

import os
os.environ['WATERCOOLER_ENVIRONMENT'] = 'test'

from datetime import datetime

from watercooler.ben.api import Api
from watercooler.hipflask import environment
from watercooler.hipflask.models import User, Status, Emotion


class TestGetStatus(unittest2.TestCase):

    def setUp(self):

        # clear database.
        assert environment.ENVIRONMENT == 'test'
        User.drop_collection()
        Status.drop_collection()
        Emotion.drop_collection()

        # create test fixtures.
        lewpen = User(first_name='Lewpen', last_name='Trippin', email='lewpen@corp.com', username='lewpen')
        lewpen.save()
        smiley = User(first_name='Smiley', last_name='Face', email='smileyface@nerds.org', username='smileyface')
        smiley.save()
        lisa = User(first_name='Lisa', last_name='Curly', email='lisa@cats.net', username='lisa')
        lisa.save()

        self.happy_emotion = Emotion(name='happy')
        self.happy_emotion.save()

        self.statuses = {
            'lewpen-morning': Status(user=lewpen, status='Morning.', date=datetime(2012,3,24,9,0)),
            'lewpen-lunch':   Status(user=lewpen, status='Lunch.',   date=datetime(2012,3,24,12,0), emotion=self.happy_emotion),
            'lewpen-evening': Status(user=lewpen, status='Evening.', date=datetime(2012,3,24,18,30)),

            'lisa-sunny': Status(user=lisa, status='Sunny morning', date=datetime(2012,3,24,7,10)),
            'lisa-happy': Status(user=lisa, status='Happy day!', date=datetime(2012,3,24,20,0), emotion=self.happy_emotion),

            'smiley-mic': Status(user=smiley, status='Two turntables and a microphone', date=datetime(2012,3,24,19,0)),
        }

        for name, status in self.statuses.iteritems():
            status.save()

    def test_get_status(self):
        """
        Get the latest status for each user.
        """
        api = Api()
        self.assertEqual(self.statuses['lewpen-evening'], api.get_status('lewpen'))
        self.assertEqual(self.statuses['lisa-happy'], api.get_status('lisa'))
        self.assertEqual(self.statuses['smiley-mic'], api.get_status('smileyface'))


if __name__ == '__main__':
    unittest2.main()
