import unittest
from temperature_tracker import TemperatureTracker
from temperature_sensor import TemperatureSensor
from unittest.mock import patch

results = [12, 22]


class TestWithPatch(unittest.TestCase):

    @patch.object(TemperatureSensor, 'check_temperature', side_effect=results)
    def test_tracks_temperature_change(self, mock):
        tracker = TemperatureTracker()
        tracker.record_initial_temperature()
        self.assertEqual(10, tracker.find_temperature_change())


if __name__ == '__main__':
    unittest.main()
