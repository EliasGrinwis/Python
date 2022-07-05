text = str(input("Enter a text: "))

counter = 0
counter_x = 0
counter_y = 0

for letter in text:
    counter += 1   
    if letter == "x":
        counter_x = counter
    if letter == "y":
        counter_y = counter

if counter_x < counter_y:
    print("In this text every x is followed by a y.")
if counter_x > counter_y:
    print("In this text not every x is followed by a y.")
