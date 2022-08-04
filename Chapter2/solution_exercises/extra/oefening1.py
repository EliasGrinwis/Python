#NEED TO FIX THIS
year = int(input("Enter a year: "))

if year % 4 == 0 and year < 1582:
    print("This is a leap year")
elif year > 1582 and year % 400 == 0 or year % 4 == 0:
    print("This is a leap year")
else:
    print("No leap year")