def euro():
        print("EURUSD is a forex currency pair")
        print("It is also the most lquiditated pair in the whole world!")

def xau():
        print("XAUUSD is a forex commaditay ")

assest = input('Type "EURUSD" or "XAUUSD" ').upper().strip()
if assest == "EURUSD":
        euro()
elif assest == "XAUUSD":
        xau()
else:
    print("Please retype the vaild answer")

