import unittest
from temperature_tracker import TemperatureTracker
from unittest.mock import Mock


class TestWithMock(unittest.TestCase):

    def test_tracks_temperature_change(self):
        tracker = TemperatureTracker()
        mock_sensor = Mock()
        tracker.sensor = mock_sensor

        mock_sensor.configure_mock(**{'check_temperature.return_value': 12})

        tracker.record_initial_temperature()
        mock_sensor.configure_mock(**{'check_temperature.return_value': 22})
        self.assertEqual(10, tracker.find_temperature_change())


if __name__ == '__main__':
    unittest.main()
