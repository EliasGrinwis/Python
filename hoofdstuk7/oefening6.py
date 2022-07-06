import random

random_number = random.randint(1, 10)

with open("FilesChapter7/wish" + str(random_number) + ".txt") as file:
    line = file.readline()

    print("Wish", random_number)
    print()
    
    while line:
        if line != "\n":
            print(line.rstrip())
        line = file.readline()
