from ApiGetter import *

btc, eur, eur_conv, btc_conv = 0, 0, 0, 0


class Wallet:

    def __init__(self):
        print("Wallet successfully initialized")

    def buy(self, money):
        global btc, eur
        btc = btc + money / get_value()
        eur = eur - money
        print("Bought ", money, "EUR worth of Bitcoin, you now have", round(btc, 4), "Bitcoins")

    def sell(self, money):
        global btc, eur
        btc = btc - money / get_value()
        eur = eur + money
        print("Sold ", money, "EUR worth of Bitcoin, you now have", round(btc, 4), "Bitcoins")

    def set_eur(self, money):
        global eur
        eur = money

    def get_eur(self):
        global eur
        return eur


    def set_btc(self, amount):
        global btc
        btc = amount

    def get_btc(self):
        global btc
        return btc

    def conv_to_eur(self):
        global eur_conv, eur, btc
        eur_conv = eur + btc * get_value()
        return eur_conv

    def conv_to_btc(self):
        global btc_conv, eur, btc
        btc_conv = btc + eur / get_value()
        return btc_conv

    def get_sum(self):
        print("You have", round(btc, 8), "BTC")
        print("You have", eur, "EUR")
        print("In total, you have ", self.conv_to_eur(), "EUR")
        print("In total, you have", self.conv_to_btc(), "BTC")