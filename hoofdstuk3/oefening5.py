
number = int(input("Enter a number: "))
counter = 1

smallest_number = number
highest_number = number

while number != 0:
    if number < smallest_number:
        smallest_number = number
    if number > highest_number:
        highest_number = number
    number = int(input("Enter a number: "))
    counter += 1

if counter == 1:
    print("No numbers entered")
else:
    print("The difference between the largest number", highest_number, "and the smallest", smallest_number, "=", abs(highest_number) + abs(smallest_number))
