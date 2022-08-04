favourite_colour = str(input("What is your favourite colour: "))

print(favourite_colour[0] + favourite_colour[2])
print("This colour consists of", len(favourite_colour), "letters")
print("")

for letter in favourite_colour:
    print(letter, "=", ord(letter))

print("")

counter = 0
while counter != len(favourite_colour):
    favourite_colour[counter]
    if counter % 2 == 0:
        print("#" + favourite_colour[counter] + "#")
    else:
        print("**" + favourite_colour[counter] + "**")

    counter += 1
