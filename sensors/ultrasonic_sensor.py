from gpiozero import DistanceSensor
import time

# Define GPIO pins for the trigger and echo pins of the ultrasonic sensor
TRIG_PIN = 18
ECHO_PIN = 24

# Set up the ultrasonic sensor with the trigger and echo pins
sensor = DistanceSensor(echo=ECHO_PIN, trigger=TRIG_PIN)

try:
    while True:
        # Read distance from ultrasonic sensor
        distance = sensor.distance * 100  # convert to centimeters

        # Print distance to console
        print("Distance: {:.2f} cm".format(distance))

        # Wait for a little bit before taking another reading
        time.sleep(0.5)

except KeyboardInterrupt:
    # Clean up GPIO pins on keyboard interrupt
    sensor.close()