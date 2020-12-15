from cryptocompy import price
import time
value1, value2, value3, stop_loss, profit, total_money = float(0), float(0), float(0), float(0), float(0), 0


def get_value():
    dvalue1 = price.get_current_price("BTC", "EUR")
    return dvalue1["BTC"]["EUR"]


def get_new_value():
    global value1, value2, value3
    value3 = value2
    value2 = value1
    value1 = get_value()
    print("Valeur 1 ", value1, "; Valeur 2 ", value2, "; Valeur 3", value3)


def buy(amount):
    global bitcoin, total_money, stop_loss
    total_money = total_money - value1 * amount
    bitcoin = bitcoin + amount
    stop_loss = value1
    print("Bought", amount, "bitcoin")


def sell(amount):
    global bitcoin, total_money
    total_money = total_money + value1 * amount
    bitcoin = bitcoin - amount
    print("Sold ", amount, "bitcoin")


def hold():
    print("Holding bitcoins for now")


def stop_loss_func():
    sell(bitcoin)
    print("Stop Loss triggered, sold everything")


def get_profit():
    print("You have", bitcoin, "BTC." )
    print("It means you have", (bitcoin*value1), "EUR.")
    print("You've made", ((bitcoin*value1) - initial_invest), "EUR ." )


def main():
    global value1, value2, value3, stop_loss
    print(bitcoin)
    while True:
        if value1 <= stop_loss:
            stop_loss_func()
        elif value3 > value2 > value1:
            sell(0.0005)
        elif value3 < value2 <value1:
            buy(0.0005)
        elif value3 > value2 < value1:
            buy(0.00025)
        elif value3 < value2 > value1:
            sell(0.00025)
        get_profit()
        get_new_value()
        time.sleep(10)




if __name__ == "__main__":
    global initial_invest, bitcoin
    initial_invest = float(input("How much do you want to invest ?"))
    bitcoin = initial_invest / get_value()  # Convert initial invest to bitcoins :D
    total_money = 0
    stop_loss = get_value() # Set initial value for the stop loss
    print("You successfully aquired", bitcoin, "BTC")  # Log to user, mainly for debug
    print("Stop Loss Value is set to ", stop_loss, "You normaly wont lose money")  # User friendly message xD
    get_new_value()
    time.sleep(10)
    get_new_value()
    time.sleep(10)
    get_new_value()
    main()

