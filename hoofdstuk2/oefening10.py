first_number = int(input("First number: "))
second_number = int(input("Second number: "))

#NEED TO FIX THIS
if first_number >= 30 and first_number <= 40 and second_number >= 30 and second_number <= 40:
    print("Both numbers are ok")
elif first_number == 65 or first_number == 72 or first_number == 83 or first_number == 90 and second_number == 65 or second_number == 72 or second_number == 83 or second_number == 90:
    print("Both numbers are ok")
else:
    print("They are NOT ok")
