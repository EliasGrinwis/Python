original_list = [0, 42, 18, 17, 0, 2, 19, 10, 5, 14]

highest_number = 0

print(original_list)

#CHECK THE HIGHEST ODD NUMBER IN THE LIST
for number in original_list:
    if number % 2 == 1:
        if number > highest_number:
            highest_number = number

#CHANGE EVERY 0 WITH THE HIGHEST ODD VALUE
counter = 0
for number in original_list:
    if number == 0:
        original_list[counter] = highest_number
    counter += 1

print(original_list)
