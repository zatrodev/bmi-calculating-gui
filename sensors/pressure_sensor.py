from gpiozero import MCP3008
import time

# Define GPIO pins for the clock, MOSI, MISO, and chip select pins of the ADC
CLK_PIN = 11
MOSI_PIN = 10
MISO_PIN = 9
CS_PIN = 8

# Set up the MCP3008 ADC with the GPIO pins
adc = MCP3008(clock_pin=CLK_PIN, mosi_pin=MOSI_PIN, miso_pin=MISO_PIN, select_pin=CS_PIN)

# Define calibration variables for the pressure sensor
V_REF = 3.3  # reference voltage in volts
V_OFFSET = 0.5  # voltage offset due to sensor's internal resistor in volts
P_OFFSET = 0  # pressure offset in kPa (can be negative)
SENSITIVITY = 4.5  # sensitivity of sensor in mV/kPa

# Define the known area of the piston in m^2 and the acceleration due to gravity in m/s^2
PISTON_AREA = 0.01  # 1 cm^2 = 0.01 m^2
GRAVITY = 9.81  # acceleration due to gravity in m/s^2

def read_pressure():
    # Read voltage from the pressure sensor
    voltage = (adc.value * V_REF) - V_OFFSET

    # Calculate pressure in kPa using the sensor's sensitivity and offset
    pressure = ((voltage / SENSITIVITY) - P_OFFSET)

    # Convert pressure to mass using the force of gravity and the known area of the piston
    mass = (pressure * PISTON_AREA) / (GRAVITY * 1000)

    return mass

try:
    while True:
        # Read mass from pressure sensor
        mass = read_pressure()

        # Print mass to console
        print("Mass: {:.2f} kg".format(mass))

        # Wait for a little bit before taking another reading
        time.sleep(0.5)

except KeyboardInterrupt:
    # Clean up GPIO pins on keyboard interrupt
    adc.close()