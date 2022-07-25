with open("Files chapter 8/sponsors.txt") as file:
    line = file.readline()

    record = line.split("*")
    print("Overview gifts")
    print("Number", "\t", "Sponsor")

    data = []

    all_lines = file.readlines()

    for line in all_lines:
        if line != "\n":
            record = line.split("*")
            data.append([record[0].rstrip()] + [record[1].rstrip()] + [record[2].rstrip()] + [record[3].rstrip()])

    print(data)

    while line:

        unique_number = record[0]
        amount_sponsored = 0
        name_sponsor = ""

        while line and record[0] == unique_number:
            amount_sponsored += int(record[3])
            name_sponsor = record[1] + ' ' + record[2]

            line = file.readline()
            record = line.split("*")
        print(unique_number, "\t", name_sponsor, amount_sponsored)

#NOT FINISHED
