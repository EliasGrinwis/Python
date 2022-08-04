with open("Files Chapter 10/first_names1ITF.txt") as file:
    line = file.readline()

    set_file = set()

    while line:
        if line != "\n":
            set_file.add(line.rstrip())
        line = file.readline()

    print("In 1ITF there are", len(set_file), "different first names")

    with open("Files Chapter 10/first_names2ITF.txt") as file2:
        line2 = file2.readline()

        set_file2 = set()

        while line2:
            if line2 != "\n":
                set_file2.add(line2.rstrip())
            line2 = file2.readline()

        print("In 2ITF there are", len(set_file2), "different first names")

        common_names = set_file.intersection(set_file2)
        print("These are the", len(common_names), "first names appearing in 1ITF and 2ITF")
        for name in sorted(common_names):
            print(name)
