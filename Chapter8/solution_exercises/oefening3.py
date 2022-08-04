with open("Files chapter 8/weather_2018 10.csv") as file:
    file.readline()
    line = file.readline()

    record = line.split(";")
    date = record[0].split(" ")

    print("Average temperatures:")

    while line:

        datum = date[0]
        average = float(record[1])
        number = 0

        while line and date[0] == datum:
            number += 1
            average += float(record[1])
            line = file.readline().rstrip()
            record = line.split(";")
            date = record[0].split(" ")

        print(datum, "\t", "number of measurements =", number, "\t", "average =", round(float(average / number), 2))

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
