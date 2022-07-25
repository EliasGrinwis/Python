import xml.etree.ElementTree as ET
root = ET.Element("compilation")

with open("Files chapter 9/songs.txt") as file:
    line = file.readline()

    while line:
        if line != "\n":
            record = line.split(';')

            #Parent
            track = ET.Element("track")
            root.append(track)

            #Child
            artist = ET.Element("artist")
            song = ET.Element("song")
            track.append(artist)
            track.append(song)

            artist.text = record[0]
            song.text = record[1]

        line = file.readline()

tree = ET.ElementTree(root)
tree.write("Files chapter 9/songs.xml")
