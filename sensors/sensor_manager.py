from sensors.ultrasonic_sensor import get_distance


class SensorManager:
    @classmethod
    def get_height():
        return get_distance()

    @classmethod
    def get_weight():
        return 60
