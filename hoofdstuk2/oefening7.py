first_number = int(input("First number: "))
smallest_number = abs(first_number)
highest_number = abs(first_number)
second_number = int(input("Second number: "))

if abs(first_number) % 5 == 0 and abs(second_number) % 5 == 0:
    if second_number < smallest_number:
        smallest_number = second_number
    print("The answer for the numbers", abs(first_number), "and", abs(second_number), "=", smallest_number)


elif abs(first_number) == abs(second_number):
    print("The answer for the numbers", abs(first_number), "and", abs(second_number), "= 0")

else:
    if abs(second_number) > abs(highest_number):
        highest_number = second_number
    print("The answer for the numbers", abs(first_number), "and", abs(second_number), "=", highest_number)
