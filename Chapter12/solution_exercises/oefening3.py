from random import randint
import xml.etree.ElementTree as ET

def read_names():
    with open("Files Chapter 12/names.txt") as file:
        line = file.readline()

        names_list = []

        while line:
            record = line.split("/")
            random_number = randint(0, 4)
            names_list.append(record[random_number].rstrip())
            line = file.readline()

        names_list.sort()
        return names_list


read_names = read_names()


def read_figures():
    xmlDoc = ET.parse("Files Chapter 12/figures.xml")
    root = xmlDoc.getroot()

    list_xml_figures = []

    for figure in root.findall("figure"):
        colour = figure.find("colour").text
        shape = figure.find("shape").text

        list_xml_figures.append(colour + ' ' + shape)

    return list_xml_figures


read_figures = read_figures()


def main(names, figures):
    print("A figure has been chosen for the following toddlers:")
    for name in names:
        length_name = len(name) - 1
        print(name, "\t", figures[length_name])


main(read_names, read_figures)
