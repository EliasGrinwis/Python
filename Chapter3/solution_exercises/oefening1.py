#DEFAULT VALUE
product = 1
number = 1
counter = -1

while number != 0:
    counter += 1
    number = int(input("Enter a number, stop by entering a zero: "))
    if number != 0:
        product = product * number

print("The product of the", counter, "numbers is", product)
