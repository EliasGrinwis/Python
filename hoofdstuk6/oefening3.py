def print_square(number, character):
    for i in range(number * number):
        print(character, end="")
        if i % number == number_input - 1:
            print()

character_input = str(input("Wich character must be used to form the lines (enter = stop): "))
if character_input != "":
    number_input = int(input("Number of characters per line = number of lines = "))

while character_input != "":
    print_square(number_input, character_input)
    character_input = str(input("Wich character must be used to form the lines (enter = stop): "))
    if character_input != "":
        number_input = int(input("Number of characters per line = number of lines = "))
