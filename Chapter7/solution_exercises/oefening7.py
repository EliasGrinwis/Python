with open("FilesChapter7/playlist.txt") as file:
    line = file.readline()

    print("playlist")
    new_list = []

    while line:
        if line != "\n":
            record = line.split(";")
            line_playlist = (record[0].rstrip(), record[1].upper().rstrip(), record[2].lower().rstrip())
            new_list.append(line_playlist)
        line = file.readline()

for playlist in new_list[::-1]:
    print(playlist[0], "\t", playlist[1], "(" + playlist[2] + ")")
