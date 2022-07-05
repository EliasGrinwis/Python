text = str(input("Pas your string of characters: "))

numbers_list = []
letters_list = []
letters_list_uppercase = []
letters_list_lowercase = []

new_list = []

for character in text:
    if character.isdigit():
        numbers_list.append(character)
    elif character != " ":
        letters_list.append(character)

for number in numbers_list:
    new_list.append(number)
for letter in letters_list:
    if letter.isupper():
        letters_list_uppercase.append(letter)
    else:
        letters_list_lowercase.append(letter)

for lower_letter in letters_list_lowercase:
    new_list.append(lower_letter)
for upper_letter in letters_list_uppercase:
    new_list.append(upper_letter)


print(new_list)