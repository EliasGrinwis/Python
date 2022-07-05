def euro_to_dollar(euro, exchange):
    print("€", euro, "= $", euro * exchange)

exchange_rate = float(input("Current dollar rate (€ -> $): "))
euro_input = float(input("Your amount in Euro: "))
euro_to_dollar(euro_input, exchange_rate)

