#CHECK IF A USER IS AN ADULT OR NOT
year_of_birth = int(input("Enter your year of birth: "))
age = int(input("Your age = "))
if age >= 18:
    print("So you're an adult.")
else:
    print("You're not an adult yet.")
