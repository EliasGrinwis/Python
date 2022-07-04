number1 = int(input("Number 1: "))
smallest_number = number1

number2 = int(input("Number 2: "))

number3 = int(input("Number 3: "))

if number2 < smallest_number:
    smallest_number = number2
if number3 < smallest_number:
    smallest_number = number3

print("The smallest number is", smallest_number)
