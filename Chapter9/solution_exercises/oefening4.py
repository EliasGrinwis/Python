import xml.etree.ElementTree as ET

xmlDoc = ET.parse("Files chapter 9/drugs.xml")
root = xmlDoc.getroot()


for leaflet in root.findall("leaflet"):
    name = leaflet.find("name")
    new_name = name.text.upper()
    pharmaceutical_forms = leaflet.find("pharmaceutical_forms")

    leaflet.remove(pharmaceutical_forms)
    name.text = new_name

xmlDoc.write("Files chapter 9/drugs_changed.xml")
