my_age = int(input("How old are you: "))
father_age = int(input("How old is your father: "))
counter = 0

while my_age * 2 < father_age:
    my_age += 1
    father_age += 1
    counter += 1
    
if counter == 0:
    print("The situation is no longer possible for your ages")
else:
    print("Within", counter, "years your father will have twice your age")
    print("Your father will be", father_age, "and you will be", my_age)
