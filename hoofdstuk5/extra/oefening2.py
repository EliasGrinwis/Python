python_classes=[['1ITFA', 35]]

python_class_B = ["1ITFB"]
python_class_C = ["1ITFC"]
python_class_D = ["1ITFD"]
python_class_E = ["1ITFE"]
python_class_F = ["1ITFF"]
python_class_G = ["1ITFG"]
python_class_H = ["1ITFH"]

python_classes.append(python_class_B)
python_classes.append(python_class_C)
python_classes.append(python_class_D)
python_classes.append(python_class_E)
python_classes.append(python_class_F)
python_classes.append(python_class_G)
python_classes.append(python_class_H)

for classes in python_classes[1:]:
    number_of_students = int(input("Number of students in " + str(classes[0]) + ": "))
    classes.append(number_of_students)

for classes in python_classes:
    print(classes)

total_students = 0

for student in python_classes:
    total_students += student[1]

print(total_students, "students follow the Python course.")
