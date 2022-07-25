with open("Files Chapter 10/local_booking.txt") as file:
    line = file.readline()

    print("Classrooms:")

    set_file = set()

    while line:
        if line != "\n":
            record = line.split(";")
            set_file.add(record[3])
        line = file.readline()

for classroom in set_file:
    print(classroom)
