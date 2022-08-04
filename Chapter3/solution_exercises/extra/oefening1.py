sequence = int(input("Up to wich limit would you like to print the sequence of Fibonacci? "))

first_number = 0
second_number = 1
new_number = 0

while new_number < sequence:
    print(new_number, end=", ")
    
    new_number = first_number + second_number #1

    first_number = second_number
    second_number = new_number #1
    
if new_number == 0:
    print("0")
