with open("FilesChapter7/weather_2018 08.csv") as file:
    file.readline()
    line = file.readline()

    record = line.split(";")
    highest_temperature = record[1]

    while line:
        if line != "\n":
            record = line.split(';')
            if record[1] > highest_temperature:
                highest_temperature = record[1]
        line = file.readline()

print("The highest temperature in this period =", highest_temperature, "°C")
