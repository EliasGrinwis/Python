with open("FilesChapter7/age_father_son.txt", "w") as file:
    file.write("""1 age_son = int(input("How old are you: "))\n""")
    file.write("""2 age_father = int(input("How old is your father: "))\n""")
    file.write("""3 counter = 0\n""")
    file.write("""4 while age_son * 2 < age_father:
5     age_son += 1
6     age_father += 1
7     counter += 1\n""")
    file.write("""8 if counter == 0:
9     print("The situation is no longer possible for your ages")
10 else:
11    print("Within", counter, 'years your father will have twice your age')
12    print("Your father will be", age_father, "and you will be", age_son)
""")
file.close()
