number1 = int(input("number 1 (0, 1 or 2): "))
number2 = int(input("number 2 (0, 1 or 2): "))
number3 = int(input("number 3 (0, 1 or 2): "))

if number1 == 2 and number2 == 2 and number3 == 2:
    print("10")

elif number1 == number2 and number2 == number3 and number1 == number3 and number1 != 2:
    print("5")
else:
    if number2 != number1 and number3 != number1:
        print("1")
    else:
        print("0")
