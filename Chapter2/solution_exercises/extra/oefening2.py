#NOT FINISHED
name = str(input("Enter your name: "))
national_number_first_9 = input("Enter the first 9 digitis of your national number: ")
national_number_last_2 = input("Enter the last 2 digits of your national number: ")
national_number = str(national_number_first_9) + str(national_number_last_2)

if len(national_number) != 11:
    print("Hello", name + ", the national number you gave is not correct")
else:
    if national_number[6] == "0" or national_number[6] == "1" or national_number[6] == "2" or national_number[6] == "3" or national_number[6] == "4":
        print("Hello", name + ", your gender is female")
    else:
        print("Hello", name + ", your gender is male")

    if national_number[4] == "0":
        print("You were born on", national_number[5] + '/' + national_number[2] + national_number[3] + '/' + national_number[0] + national_number[1])
    else:
        print("You were born on", national_number[4] + national_number[5] + '/' + national_number[2] + national_number[3] + '/' + national_number[0] + national_number[1])
