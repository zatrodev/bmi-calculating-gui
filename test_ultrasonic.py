from sensors.ultrasonic_sensor import get_distance

while (True):
    print(1.92 - get_distance() - 0.22)
