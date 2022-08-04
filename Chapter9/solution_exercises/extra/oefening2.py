import xml.etree.ElementTree as ET

xmlDoc = ET.parse("../Files chapter 9/customers.xml")
root = xmlDoc.getroot()

for customer in root.findall("customer"):
    language = customer.get("language")
    discount = customer.get("discount")

    customer.attrib = {}

    name = customer.find("name")

    name.set("language", language)

    discount_element = ET.Element("discount")
    discount_element.text = discount
    customer.append(discount_element)

xmlDoc.write("../Files chapter 9/new_customers.xml")
