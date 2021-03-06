from time import sleep

from cryptocompy import price

value1, value2, value3 = 0, 0, 0


def get_value():
    dace1 = price.get_current_price("BTC", "EUR")
    return dace1["BTC"]["EUR"]


def get_new_value():
    global value1, value2, value3
    value3 = value2
    value2 = value1
    value1 = get_value()
    print("Valeur 1 ", value1, "; Valeur 2 ", value2, "; Valeur 3", value3)
    return value1, value2, value3


def get_values():
    global value1, value2, value3
    return value1, value2, value3


def get_initial_values(delay):
    global value1, value2, value3
    get_new_value()
    sleep(delay)
    get_new_value()
    sleep(delay)
    return get_new_value()
