with open("FilesChapter7/hamlet.txt") as hamlet:
    line = hamlet.readline()

    total_characters_hamlet2 = 0

    with open("FilesChapter7/hamlet2.txt", "w") as hamlet2:
        while line:
            if line != "\n":
                single_space = " ".join(line.split())
                hamlet2.write(single_space + "\n")
                print(line.rstrip())
            line = hamlet.readline()

            total_characters_hamlet2 += len(single_space)


with open("FilesChapter7/hamlet2.txt") as hamlet3:
    line_hamlet_2 = hamlet3.readline()

    total_characters_hamlet3 = 0

    with open("FilesChapter7/hamlet3.txt", "w") as hamlet4:
        while line_hamlet_2:
            if line_hamlet_2 != "\n":
                for i in "aeiouAEIOU":
                    line_hamlet_2 = line_hamlet_2.replace(i, "")
            line_hamlet_2 = hamlet3.readline()

            total_characters_hamlet3 += len(line_hamlet_2)


print(total_characters_hamlet2)
print(total_characters_hamlet3)
