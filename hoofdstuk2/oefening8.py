#CHECK IF A PARTY IS STUPID GOOD OR FANTASTIC
bottles_of_wine = int(input("How many bottles of wine are there: "))
pizzas = int(input("How many pizzas are there: "))

if pizzas > (bottles_of_wine * 2):
    print("This is a fantastic party")
elif pizzas >= 5 and bottles_of_wine >= 5:
    print("This is a good party")
else:
    print("This is just a stupid party")
