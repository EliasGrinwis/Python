import xml.etree.ElementTree as ET

xmlDoc = ET.parse("Files chapter 9/cinemas.xml")
root = xmlDoc.getroot()

print("Bioscopen in Antwerpen")
for bioscoopoverzicht in root.findall("bioscoopoverzicht"):
    district = bioscoopoverzicht.find("district").text

    if district == "Antwerpen":
        naam = bioscoopoverzicht.find("naam").text
        straat = bioscoopoverzicht.find("straat").text
        huisnummer = bioscoopoverzicht.find("huisnummer").text
        postcode = bioscoopoverzicht.find("postcode").text
        print(naam)
        print(straat, huisnummer)
        print(postcode, district)
        print("")
