from hx711 import HX711


try:
    hx711 = HX711(dout_pin=12, pd_sck_pin=11)

    err = hx711.zero()
    if err:
        raise ValueError('Tare is unsuccessful.')

    while True:
        print(hx711.get_raw_data_mean())
except (KeyboardInterrupt, SystemExit):
    print("Exiting...")
