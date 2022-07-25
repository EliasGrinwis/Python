import xml.etree.ElementTree as ET

xmlDoc = ET.parse("Files chapter 9/plants.xml")
root = xmlDoc.getroot()

counter = 1
for plant in root.findall("plant"):
    light = plant.find("light").text

    if light == "SUN":
        common = plant.find("common").text
        botanical = plant.find("botanical").text

        print("Plant", counter, ":", common, "(" + botanical.capitalize() + ")")
        counter += 1
