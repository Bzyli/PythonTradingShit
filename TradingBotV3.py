from Wallet import *
from ApiGetter import *


def get_variation():
    if not is_it_possible(): return
    if get_values()[0] > get_values()[1] > get_values()[2]:  # Not stonks
        return 0
    elif get_values()[0] < get_values()[1] < get_values()[2]:  # Stonks
        return 1
    elif get_values()[0] > get_values()[1] < get_values()[2]:  # Curve Draws a V
        return 2
    elif get_values()[0] < get_values()[1] > get_values()[2]:  # Curve Draws a "Mountain"
        return 3
    else:
        return 4


def is_it_possible():
    if wallet.get_eur() <= 0:
        return False


def action_order(action, amount):
    if action == 0: wallet.buy(amount)
    elif action == 1: wallet.sell(amount)
    elif action == 2: wallet.buy(amount)
    elif action == 3: wallet.sell(amount)
    elif action == 4: print("Holding...")


def main():
    while True:
        action_order(get_variation(), 10)
        wallet.get_sum()
        sleep(delay)


def test():
    wallet = Wallet()
    delay = int(input("At what rate do you wanna trade in seconds"))
    wallet.buy(float(input("How much do you wanna invest")))
    wallet.set_eur(0)
    get_initial_values(delay)
    main()


if __name__ == "__main__":
    wallet = Wallet()
    delay = int(input("At what rate do you wanna trade in seconds"))
    wallet.buy(float(input("How much do you wanna invest")))
    wallet.set_eur(0)
    get_initial_values(delay)
    main()
