from sensors.ultrasonic_sensor import get_distance

HEIGHT_FROM_GROUND = 1.95


class SensorManager:
    @staticmethod
    def get_height():
        return get_distance()

    @staticmethod
    def get_weight():
        return 60
