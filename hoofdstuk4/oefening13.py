
name = str(input("Your name (press enter to stop): "))

while name != "":
    print("")
    menu = "Menu:"
    print(menu)
    print("*" * len(menu))
    print("U Uppercase")
    print("L Lowercase")
    print("A Alternate")
    choice = ""
    while choice != "U" and choice != "L" and choice != "A":
        choice = str(input("Make a choice (U-L-A): ")).upper()
        if choice == "U" :
            print(name.upper())
        if choice == "L":
            print(name.lower())
        if choice == "A":
            counter = 0
            for letter in name:
                if counter % 2 == 0:
                    print(letter.upper(), end="")
                else:
                    print(letter.lower(), end="")
                counter += 1
            print("")
    name = str(input("Your name (press enter to stop): "))

else:
    print("")
