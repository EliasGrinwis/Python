def all_possible_classes():
    with open("Files Chapter 12/classlist.csv") as file:
        line = file.readline()

        all_classes_list = []

        while line:
            record = line.split(";")
            if line != "\n":
                all_classes_list.append(record[3].rstrip())
            line = file.readline()

        unique_classes_list = set(all_classes_list)

        print(unique_classes_list)

        return unique_classes_list


def control(classname):
    with open("Files Chapter 12/classlist.csv") as file:
        line = file.readline()

        student_is_present = []

        while line:
            record = line.split(";")
            if record[3].rstrip() == classname:
                if line != "\n":
                    check_if_person_present = str(input(record[2] + ' ' + record[1] + ': ')).lower()
                    if check_if_person_present == "n":
                        student_is_present.append(record[1] + ';' + record[2] + ";NOT")
                    if check_if_person_present == "":
                        student_is_present.append(record[1] + ';' + record[2] + ";OK")
            line = file.readline()
        if len(student_is_present) == 0:
            return "does_not_exists"
        else:
            return student_is_present


def main():
    all_possible_classes()
    class_name = str(input("In which class do you want to do a check: "))
    list_control = control(class_name)
    if list_control == "does_not_exists":
        print("This class doesn't exit")
    else:
        with open("Files Chapter 12/" + class_name + '.csv', 'w') as file:
            file.write("Attendance list " + str(class_name) + "\n")
            for i in range(len(list_control)):
                file.write(list_control[i] + "\n")
            print("")


main()
