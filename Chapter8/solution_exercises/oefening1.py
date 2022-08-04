with open("Files chapter 8/classrooms.txt") as file:
    line = file.readline().rstrip()
    record = line.split(';')

    while line:
        class_room = record[2]
        total_students = 0

        print(class_room)
        while line and record[2] == class_room:
            total_students += 1
            line = file.readline().rstrip()
            record = line.split(";")
            print("\t", record[1], record[0])
        print("Number of students in classroom", class_room, "=", total_students)
