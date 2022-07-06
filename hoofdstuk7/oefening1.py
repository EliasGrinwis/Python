with open("FilesChapter7/first_names.txt") as file:
    line = file.readline()
    counter = 0
    counter_z_letter = 0
    while line:
        line = file.readline()
        if "Z" in line or "z" in line:
            counter_z_letter += 1
            if line != "\n":
                print(line.rstrip())
        counter += 1

print("There are", counter, "first names in the file.")
print(counter_z_letter, "of which contain a letter z")
