import unittest2

import os
os.environ['WATERCOOLER_ENVIRONMENT'] = 'test'

from watercooler.ben.api import Api
from watercooler.hipflask import environment
from watercooler.hipflask.models import User, Status, Emotion


class TestAddStatus(unittest2.TestCase):

    def setUp(self):

        # clear database.
        assert environment.ENVIRONMENT == 'test'
        User.drop_collection()
        Status.drop_collection()

        # create test fixtures.
        self.user = User(first_name='Lewpen', last_name='Trippin', email='lewpen@corp.com', username='lewpen')
        self.user.save()

        self.sad_emotion = Emotion(name='sad')
        self.sad_emotion.save()


    def test_add_status(self):
        """Add a status for user."""

        self.assertEqual([], list(Status.objects))

        api = Api()
        api.add_status(status='I was wanting you to love me.', user=self.user)

        # verify that the status was inserted successfully.
        status = Status.objects.first()
        self.assertIsNotNone(status)
        self.assertEqual(status.status, 'I was wanting you to love me.')
        self.assertEqual(status.user, self.user)
        self.assertEqual(status.emotion, None)

    def test_add_status_with_emotion(self):
        """Add a status with an emotion."""

        self.assertEqual([], list(Status.objects))

        api = Api()
        api.add_status(status='I was wanting you to love me.', user=self.user, emotion=self.sad_emotion)

        # verify that the status was inserted successfully.
        status = Status.objects.first()
        self.assertIsNotNone(status)
        self.assertEqual(status.status, 'I was wanting you to love me.')
        self.assertEqual(status.user, self.user)
        self.assertEqual(status.emotion, self.sad_emotion)





if __name__ == '__main__':
    unittest2.main()
