import random

random_number = random.randint(1, 10)

tables = []

for i in range(10):
    i += 1
    tables.append(str(i) + " x " + str(random_number) + " = " + str(i * random_number))

with open("FilesChapter7/table_" + str(random_number) + ".txt", "w") as file:
    for table in tables:
        file.write(table + "\n")
