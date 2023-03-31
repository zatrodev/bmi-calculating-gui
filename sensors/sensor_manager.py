from sensors.ultrasonic_sensor import get_distance

HEIGHT_FROM_GROUND = 1.92


class SensorManager:
    @staticmethod
    def get_height():
        return HEIGHT_FROM_GROUND - get_distance()

    @staticmethod
    def get_weight():
        return 60
