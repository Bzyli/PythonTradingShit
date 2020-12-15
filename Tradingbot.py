from cryptocompy import price
import time

firstLastValue, second_last_value, actual_value = 0, 0, 0
bitcoins = 1


def getFirstLastValue():
    dict1 = price.get_current_price("BTC", "EUR")
    firstLastValue = dict1["BTC"]["EUR"]
    return dict1["BTC"]["EUR"]


def getSecondLastValue():
    dict2 = price.get_current_price("BTC", "EUR")
    second_last_value = dict2["BTC"]["EUR"]
    return dict2["BTC"]["EUR"]


def getActualValue():
    dict3 = price.get_current_price("BTC", "EUR")
    actual_value = dict3["BTC"]["EUR"]
    return dict3["BTC"]["EUR"]
# bon eum je vais pas pouvoir trop t'aider car pour moi là c'est eum comment dire pas très très beau pour ok np je vais rewrite en respectant tout mais tu veux voir un truc drole ? pour le run je dois lancer un autre script xDDDD
def did_it_stonks(first_last_value, second_last_value,
                  actual_value):  # c'est quoi le problème ? je veux que lmes variables se décalle : secondlastvlaue prend l'ancienne valeur de actual et firstlast l'ancienne de second last  bref t'as capté
    # mec wtf ton code on est en python tu sais ?
    #
    if first_last_value < second_last_value and second_last_value < actual_value:
        print("Turbo Stonks")
    elif first_last_value < second_last_value and second_last_value > actual_value:
        print("Confused Stonks /")
    elif first_last_value > second_last_value > actual_value:
        print("not stonks")
    else:
        print("Confused Stonks \/ ")

    first_last_value = second_last_value
    second_last_value = actual_value
    actual_value = getActualValue()
    print(first_last_value)
    print(second_last_value)
    print(actual_value)


def conv_bitcoin_eur():
    print("ur $ : ", getFirstLastValue() * bitcoins)
    return (getFirstLastValue() * bitcoins)


def mainLoop():
    while True:
        did_it_stonks(0, 0, 0)
        conv_bitcoin_eur()
        print(bitcoins)
        time.sleep(10)




if __name__ == "__main__":
    mainLoop()
    # bon bah voilà non? noice thx ♥ je vais me debrouiller pour le reste