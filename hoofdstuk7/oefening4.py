with open("FilesChapter7/irish_song.txt") as file:
    line = file.readline()

    shortest_line = len(line.rstrip())
    shortest_sentence = ""
    while line:
        if line != "\n":
            if len(line.rstrip()) < shortest_line:
                shortest_line = len(line.rstrip())
                shortest_sentence = line.rstrip()
        line = file.readline()

print("The shortest line has", shortest_line, "characters")
print(shortest_sentence)
