from os.path import exists

def read_month():
    month = 0
    while month > 12 or month < 1:
        month = int(input("Choose a month: "))
        if month == 8:
            month = "0" + str(month)

        if exists("../FilesChapter7/weather_2018 " + str(month) + ".csv"):
            return month

        elif not exists("../FilesChapter7/weather_2018 " + str(month) + ".csv") and 12 >= month >= 1:
            return "No data available for this month"


read_month = read_month()


if type(read_month) == int or read_month == "08":
    print()
    with open("../FilesChapter7/weather_2018 " + str(read_month) + ".csv") as file:
        file.readline()
        line = file.readline()

        new_list = []
        record = line.split(";")
        highest_temperature = float(record[1])
        time_stamp = ""
        date = ""

        while line:
            if line != "\n":
                record = line.split(';')
                tijdstip = record[0].split(' ')

                if float(record[1]) > float(highest_temperature):
                    highest_temperature = float(record[1])
                    time_stamp = tijdstip[1]
                    date = tijdstip[0]

                new_list.append(record[0])
            line = file.readline()

        period = "Period"
        print(period + ":", "\t", new_list[0], "-", new_list[-1])
        print("-" * len(period))
        print("The highest temperature in this period =", highest_temperature, "°C")
        print("This temperature was measured at", time_stamp + "h on", date)
else:
    print(read_month)
