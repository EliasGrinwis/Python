print("Enter your name and the distance to school.")
print("Type stop when you want to close the entry.")

name = ""

name_list = []
distance_list = []

while name != "stop":
    name = str(input("Your name: "))
    if name != "stop":
        name_list.append(name)
        distance = float(input("Distance to school: "))
        distance_list.append(distance)

if name == "stop" and len(name_list) == 0:
    print("")
else:
    print("Overview")
    
    highest_number = 0
    person = ""

    for name, distance in zip(name_list, distance_list):
        if distance > highest_number:
            highest_number = distance
            person = name

        print(name, "\t", distance)

    print(person, "lives the farthest, namely", highest_number, "km")
    print("The average distance is", sum(distance_list) / len(distance_list))
