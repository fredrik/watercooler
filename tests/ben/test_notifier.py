import unittest2
from mock import patch

import requests

from watercooler.ben.notifier import NodeNotifier


class TestNodeNotifier(unittest2.TestCase):
    def setUp(self):
        pass
    def test_notify(self):
        """
        Test that NodeNotifier sends a POST request to the specfied remote listener.
        """
        with patch.object(requests, 'post') as mock_method:
            notifier = NodeNotifier(remote_address='http://localhost:8800')
            notifier.notify(username='wayne.coyne')
            mock_method.assert_called_with(
                'http://localhost:8800/new_status',
                {'username': 'wayne.coyne'},
            )

if __name__ == '__main__':
    unittest2.main()
