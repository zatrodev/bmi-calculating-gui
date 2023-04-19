from sensors.ultrasonic_sensor import get_distance
from sensors.pressure_sensor import setup_sensor
from sensors.pressure_sensor import get_weight_reading

first_try = True


class SensorManager:
    @staticmethod
    def get_height():
        return get_distance()

    @staticmethod
    def get_weight():
        if first_try:
            setup_sensor()
            first_try = False

        return get_weight_reading()
