original_list = [9, 17, 25, 4, 12, 7]

new_list = []
odd_list = []

for number in original_list:
    if number % 2 == 0:
        new_list.append(number)
    else:
        odd_list.append(number)

for number in odd_list:
    new_list.append(number)

print(original_list, "becomes", new_list)
