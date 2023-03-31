from pyA20.gpio import gpio
from pyA20.gpio import port
import time

TRIG = port.PA7
ECHO = port.PA8

gpio.init()

gpio.setcfg(TRIG, gpio.OUTPUT)
gpio.setcfg(ECHO, gpio.INPUT)


def get_distance():
    gpio.output(TRIG, 0)

    print("Waiting For Sensor To Settle")

    time.sleep(2)
    gpio.output(TRIG, 1)
    time.sleep(0.00001)
    gpio.output(TRIG, 0)

    while gpio.input(ECHO) == 0:
        pulse_start = time.time()

    while gpio.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    return (distance / 100) + 0.2
