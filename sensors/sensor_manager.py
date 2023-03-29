from pyA20.gpio import gpio

from sensors.ultrasonic_sensor import get_distance


class SensorManager:
    def __init__(self):
        gpio.init()

    def get_height(self):
        return get_distance()

    def get_weight(self):
        return 60


sensor_manager = SensorManager()
