with open("FilesChapter7/contacts.csv") as file:
    line = file.readline()

    counter_woman = 0
    list_girls = []

    counter_man = 0
    list_boys = []

    while line:
        if line != "\n":
            record = line.split(';')
            if record[3].rstrip() == "M":
                counter_man += 1
                list_boys.append(record[1] + ' ' + record[0])

            if record[3].rstrip() == "V":
                counter_woman += 1
                list_girls.append(record[1] + ' ' + record[0])

        line = file.readline()

print(counter_woman, "girls:")
for girl in sorted(list_girls):
    print("\t", girl)

print(counter_man, "boys:")
for boy in sorted(list_boys):
    print("\t", boy)
