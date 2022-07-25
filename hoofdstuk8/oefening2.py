with open("Files chapter 8/courses.csv") as file:
    file.readline()
    line = file.readline()
    record = line.split(";")

    with open("Files chapter 8/students.csv", "w") as student_information:

        while line:

            student_number = record[3]

            while line and record[3] == student_number:
                if line != "\n":
                    print(record[3].rstrip() + ";" + record[4].rstrip() + ";" + record[5].rstrip() + ";" + record[1].rstrip() + " (" + record[2].rstrip() + ")", end=" ")
                    student_information.write(record[3].rstrip() + ";" + record[4].rstrip() + ";" + record[5].rstrip() + ";" + record[1].rstrip() + " (" + record[2].rstrip() + ")" + "\n")
                line = file.readline()
                record = line.split(";")

            print()

#NOT FINISHED
