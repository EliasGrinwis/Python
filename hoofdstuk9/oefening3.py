import xml.etree.ElementTree as ET

xmlDoc = ET.parse("Files chapter 9/jobs.xml")
root = xmlDoc.getroot()

print("Overview IT vacancies:")
print("")
counter = 1

for jobs in root.findall("jobs"):
    for company in jobs:
        name = company.find("name").text
        vacancies = company.find("vacancies")
        contact = company.find("contact")
        email = contact.find("email").text

        for vacancy in vacancies:
            for position in vacancy:
                group = position.get("group")
                if group == "IT":
                    print(str(counter) + "." + "\t" + "Position:" + "\t" + position.text)
                    print("\t" + "Company:" + "\t" + name)
                    print("\t" + "Contact:" + "\t" + email)
                    counter += 1
                    print("")
