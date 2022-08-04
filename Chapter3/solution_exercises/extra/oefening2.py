print("Press Enter for each new striker you see.")
print("If you want to pass a group, enter the number of strikers")
print("If you want to stop, typ S and press Enter")

strikers = 0

input_user = str(input(">> "))
confirmation = ""

while input_user != "S":
    if input_user == "":
        strikers += 1
    else:
        strikers += int(input_user)
    input_user = str(input(">> "))
    if input_user == "S":
        confirmation = str(input("Do you really want to stop Y/N? ")).lower()
        if confirmation == "n":
            input_user = ""
            strikers -= 1

print("Total number of strikers =", strikers)
