from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector
from hx711 import HX711

# Set up the HX711 sensor
hx711 = HX711(dout=port.PA12, pd_sck=port.PA11)
hx711.set_reading_format("MSB", "MSB")
hx711.set_reference_unit(1)
hx711.reset()

# Read the weight
weight = hx711.get_weight()

# Print the weight
print("Weight: {} grams".format(weight))
