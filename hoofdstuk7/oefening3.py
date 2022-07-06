with open("FilesChapter7/first_names.txt") as file:
    line = file.readline()
    counter = 0
    while line:
        print(line.rstrip(), end=" ")
        if counter % 10 == 9:
            print()
        line = file.readline()
        counter += 1
