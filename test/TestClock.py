import unittest
import clock
from unittest.mock import patch


class MyTestCase(unittest.TestCase):

    @patch('time.time', return_value=1571871846.8861961)
    def test_the_time(self, mock):
        self.assertEqual(clock.whats_the_time(), 1571871846.8861961)


if __name__ == '__main__':
    unittest.main()
