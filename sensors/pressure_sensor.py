from hx711 import HX711
from pyA20.gpio import port


try:
    hx711 = HX711(dout_pin=port.PA12, pd_sck_pin=port.PA11)

    # err = hx711.zero()
    # if err:
    #     raise ValueError('Tare is unsuccessful.')

    while True:
        print(hx711.get_weight_mean())
except (KeyboardInterrupt, SystemExit):
    print("Exiting...")
