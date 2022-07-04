#lets learn about lists


supplies = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows", "tent"]


camp_site = ["Crystal Lake", 404, 95.5, 10, False]


counter = -1

print(supplies)

for item in supplies:
    counter += 1
    if item == "knife":
        supplies.remove(supplies[counter])


print(supplies)
my_list = []
