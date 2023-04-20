from sensors.ultrasonic_sensor import get_distance
from sensors.pressure_sensor import setup_sensor
from sensors.pressure_sensor import get_weight_reading


class SensorManager:
    first_try = True

    @staticmethod
    def get_height():
        return get_distance()

    @staticmethod
    def get_weight():
        if SensorManager.first_try:
            setup_sensor()
            SensorManager.first_try = False

        return get_weight_reading()
