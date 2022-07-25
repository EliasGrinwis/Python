months = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

month_input = " "

while month_input != "":
    month_input = str(input("Month (press Enter if you want to see an overview of all months): "))

    right_input = ""

    for month in months:
        if month_input == month:
            right_input = month
            print(months[month])

    if right_input == "":
        print("This month does not exist.")

    
for month in months:
    print(month, "\t", months[month])
