import random

random_number = random.randint(1, 15)
guess_number = int(input("Enter a positive number: "))
counter = 1

while guess_number != random_number:
    
    if guess_number < random_number:
        print("Higher!")
    else:
        print("Lower!")

    guess_number = int(input("Enter a positive number: "))
    counter += 1
    
print("You have guessed the number", random_number, "in", counter, "turns.")
