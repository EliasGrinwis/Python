word = str(input("What do you ear for lunch: "))

if word[:8] == "sandwich" and word[-8:] == "sandwich":
    print("You have", word[8: -8], "between your sandwich")
else:
    print("")
