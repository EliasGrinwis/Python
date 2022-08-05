def read_books():
    with open("Files Chapter 12/books.txt") as file:
        line = file.readline()

        list_books = []

        while line:
            if line != "\n":
                list_books.append(line.rstrip())
            line = file.readline()
        return list_books


list_books = read_books()


def make_a_choice():
    choice = ""

    while choice != "s" and choice != "a" and choice != "b" and choice != "c":
        print("a - Overview")
        print("b - Longest title")
        print("c - 5 letters on a row")
        print("s - stop")
        choice = str(input("Make your choice: ")).lower()

    return choice


make_a_choice = make_a_choice()


def main(choice, list_books):
    if choice == "a":
        print("List of books:")
        print()
        counter = 1
        for i in range(len(list_books)):
            print(counter, list_books[i])
            counter += 1
    if choice == "b":
        print("List of books:")
        print()
        counter = 1
        longest_charachters = 0
        for i in range(len(list_books)):
            if len(list_books[i]) > longest_charachters:
                longest_charachters = len(list_books[i])
            print(counter, list_books[i])
            counter += 1
        print()
        print("The longest title has", longest_charachters, "characters")
    if choice == "c":
        booknumber = int(input("Enter booknumber max 10: "))
        for i in range(len(list_books[booknumber - 1])):
            print(list_books[booknumber - 1][i], end="")
            if i % 5 == 4:
                print()


main(make_a_choice, list_books)
