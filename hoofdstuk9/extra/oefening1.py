import xml.etree.ElementTree as ET

xmlDoc = ET.parse("../Files chapter 9/plants.xml")
root = xmlDoc.getroot()

print("List of plants, sorted by")


def make_a_choice():
    choice = ""

    while choice != "A" and choice != "H" and choice != "L":
        print("\t" + "A: Alphabet")
        print("\t" + "H: Price (high to low)")
        print("\t" + "L: Price (low to high")
        choice = str(input("Your choice: ")).upper()
    return choice


make_a_choice = make_a_choice()
#print(make_a_choice)


def making_a_list():
    data_xml_file = []

    for plant in root.findall("plant"):
        common = plant.find("common").text
        price = plant.find("price").text

        list_common_and_price = [common, price]

        data_xml_file.append(list_common_and_price)
        #print(common)
        #print(price)

    return data_xml_file


making_a_list = making_a_list()


def result():
    if make_a_choice == "A":
        for line in sorted(making_a_list):
            print(line[1], "|", line[0])

    if make_a_choice == "H":
        def itemgetter(price):
            return price[1]

        making_a_list.sort(key=itemgetter, reverse=True)

        for line in making_a_list:
            print(line[1], "|", line[0])

    if make_a_choice == "L":
        def itemgetter(price):
            return price[1]

        making_a_list.sort(key=itemgetter)

        for line in making_a_list:
            print(line[1], "|", line[0])


result()
