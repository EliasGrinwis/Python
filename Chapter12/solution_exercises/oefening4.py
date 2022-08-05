def lowest_price():
    with open("Files Chapter 12/prices.txt") as file:
        line = file.readline().rstrip()
        record = line.split(";")

        name_and_lowest_price = {}

        while line:
            lowest_price = record[1]
            name = record[0]

            while line and record[0] == name:
                record = line.split(";")

                if record[1] <= lowest_price:
                    lowest_price = record[1]

                line = file.readline()
            name_and_lowest_price[name] = lowest_price

        return name_and_lowest_price


lowest_price = lowest_price()
print(lowest_price)


def main():
    make_a_choice = str(input("Enter the item (press x if you want to stop): ")).lower()

    while make_a_choice != "x":
        check_if_word_exists = []
        for word in lowest_price:
            check_if_word_exists.append(word)

        if make_a_choice not in check_if_word_exists:
            print("This item is not available.")
        else:
            print("The lowest price of", make_a_choice, "is", lowest_price[make_a_choice], "EUR")
        make_a_choice = str(input("Enter the item (press x if you want to stop): ")).lower()


main()
