number = int(input("Enter a number: "))

for i in range(number + 1):
    if number == 0:
        print(number, end="")
    else:
        print(number, end=" ... ")
    number -= 1
