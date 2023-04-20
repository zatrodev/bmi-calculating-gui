from sensors.hx711 import HX711  # import the class HX711

hx = HX711(dout_pin=7, pd_sck_pin=8)


def setup_sensor():
    err = hx.zero()
    if err:
        raise ValueError('Tare is unsuccessful.')

    reading = hx.get_raw_data_mean()
    if reading:
        print('Data subtracted by offset but still not converted to units:',
              reading)
    else:
        print('invalid data', reading)

    input('Put known weight on the scale and then press Enter')
    reading = hx.get_data_mean()
    if reading:
        print('Mean value from HX711 subtracted by offset:', reading)
        known_weight_grams = input(
            'Write how many grams it was and press Enter: ')
        try:
            value = float(known_weight_grams)
            print(value, 'grams')
        except ValueError:
            print('Expected integer or float and I have got:',
                  known_weight_grams)

        ratio = reading / value
        hx.set_scale_ratio(ratio)
        print('Ratio is set.')
    else:
        raise ValueError(
            'Cannot calculate mean value. Try debug mode. Variable reading:', reading)


def get_weight_reading():
    return round(hx.get_weight_mean() / 1000, 2)
