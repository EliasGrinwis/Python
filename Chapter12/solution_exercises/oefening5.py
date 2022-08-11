import numpy as np
from matplotlib import pyplot as plt
import xml.etree.ElementTree as ET


def read_txt(file_name):
    temperature = np.loadtxt(fname=file_name, dtype=int, delimiter=";", skiprows=1)

    userID_array = np.array(temperature[:, 0], str)
    tank_array = np.array(temperature[:, 1])
    damage_array = np.array(temperature[:, 2])
    support_array = np.array(temperature[:, 3])

    full_array = []

    for userID, tank, damage, support in zip(userID_array, tank_array, damage_array, support_array):
        full_array.append([userID, tank, damage, support])

    return full_array


read_txt = read_txt("Files Chapter 12/games.csv")


def read_xml(file_name):
    xmlDoc = ET.parse(file_name)
    root = xmlDoc.getroot()

    xml_list = []

    for row in root.findall("ROW"):
        userID = str(row.find("userID").text)
        battleTag = str(row.find("battleTag").text)
        xml_list.append([userID, battleTag])
    return xml_list


read_xml = read_xml("Files Chapter 12/users.xml")
print(read_xml)


def main():
    games = np.array(read_txt)
    users = np.array(read_xml)

    print(games[:, 0])
    print(games[:, 1])

    print(users)
    plt.figure(figsize=(10, 3))

    plt.suptitle(users[1][1])

    plt.subplot(131)
    plt.xticks(range(0, 60, 20))
    plt.yticks(range(1800, 2400, 100))
    plt.plot(games[1])
    plt.legend("Tank",)

    plt.subplot(132)
    plt.plot(games[2])
    plt.yticks(range(1800, 2300, 100))
    plt.xticks(range(0, 60, 20))

    plt.subplot(133)
    plt.plot(games[3])
    plt.yticks(range(1750, 2300, 100))
    plt.xticks(range(0, 60, 20))
    plt.show()


main()
