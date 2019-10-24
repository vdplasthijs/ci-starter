from temperature_sensor import TemperatureSensor


class TemperatureTracker:

    def __init__(self) -> None:
        self.sensor = TemperatureSensor()
        self.start_temp = 0

    def record_initial_temperature(self):
        self.start_temp = self.sensor.check_temperature()

    def find_temperature_change(self):
        return self.sensor.check_temperature() - self.start_temp
