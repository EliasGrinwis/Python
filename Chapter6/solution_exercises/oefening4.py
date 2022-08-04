import random

def generate_list(total_numbers, lowest_number, highest_number):
    new_list = []
    counter = 0
    while counter != total_numbers:
        random_number = random.randint(lowest_number, highest_number)
        new_list.append(random_number)
        counter += 1
    return new_list


def filter(list):
    filtered_list = []
    for number in list:
        if number not in filtered_list:
            filtered_list.append(number)
    return filtered_list


generate_list = generate_list(5, 1, 5)

print("You threw: ", generate_list)
print("Your unique rolls were: ", filter(generate_list))
