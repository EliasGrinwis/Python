with open("FilesChapter7/first_names.txt") as file:
    line = file.readline()

    new_list = []
    while line:
        if line != "\n":
            new_list.append(line.rstrip())
        line = file.readline()

for name in new_list[::-1]:
    print(name)
