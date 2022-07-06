with open("FilesChapter7/books.txt") as file:
    line = file.readline()

    counter = 0

    while line:

        if line != "\n":
            if counter % 2 == 0:
                if counter == 0:
                    counter = 1
                    print(counter, line.rstrip(), "-> ", end="")
                    counter = 0
                else:
                    print(round(counter / 2), line.rstrip(), "-> ", end="")
            else:
                print(line.rstrip())

        line = file.readline()
        counter += 1

