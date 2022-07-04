final_digit = int(input("What final digit do you want to check the numbers on: "))

counter = 0
check_digit = 0

while counter != 10:
    number = int(input("Enter a number: "))
    counter += 1
    if number % 10 == final_digit:
        check_digit += 1

print(check_digit, "out of 10 numbers ends on", final_digit)
