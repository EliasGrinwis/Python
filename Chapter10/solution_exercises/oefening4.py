with open("Files Chapter 10/games.txt") as file:
    line = file.readline()

    set_txt_file = set()

    while line:
        record = line.split(",")
        if line != "\n":
            set_txt_file.add(record[7].rstrip())
        line = file.readline()

import xml.etree.ElementTree as ET

xmlDoc = ET.parse("Files Chapter 10/games.xml")
root = xmlDoc.getroot()


set_xml_file = set()

for game in root.findall("game"):
    type = game.find("type").text
    set_xml_file.add(type)

print(set_txt_file)
print(set_xml_file)

print("In the txt-file:", len(set_txt_file), "types of games")
print("IN the xml-file:", len(set_xml_file), "types of games")
print("")
print("The types that occur in both files:")
print(set_xml_file.intersection(set_txt_file))
print("")
print("The types that only appear in the txt-file:")
print(set_txt_file.difference(set_xml_file))
print("")
print("The types that only appear in the xml-file")
print(set_xml_file.difference(set_txt_file))
