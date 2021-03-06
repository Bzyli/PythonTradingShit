from Wallet import *
from ApiGetter import *


class TradingClass(object):

    def __init__(self, value, rate):
        wallet = Wallet()
        wallet.buy(self, (float(value)))
        wallet.set_eur(0)
        self.delay = rate
        get_initial_values(self.delay)
        self.main()

    def get_variation(self):
        if not self.is_it_possible(): return
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

    def is_it_possible(self):
        if self.wallet.get_eur() <= 0:
            return False

    def action_order(self, action, amount):
        if action == 0: self.wallet.buy(amount)
        elif action == 1: self.wallet.sell(amount)
        elif action == 2: self.wallet.buy(amount)
        elif action == 3: self.wallet.sell(amount)
        elif action == 4: print("Holding...")

    def main(self):
        while True:
            self.action_order(self.get_variation(), 10)
            self.wallet.get_sum()
            sleep(self.delay)
