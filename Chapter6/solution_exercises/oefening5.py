def counts_upper_and_lower(text):
    upper_list = []
    lower_list = []
    new_list = []
    for letter in text:
        if letter.isupper():
            upper_list.append(letter)
        elif letter != " ":
            lower_list.append(letter)

    new_list.append(len(upper_list))
    new_list.append(len(lower_list))

    return new_list

#INPUT
text = ""

#CALCULATION
new_list = counts_upper_and_lower(text)

#OUTPUT
while new_list[0] < 2 or new_list[1] < 3:
    text = str(input("Set your password (at least 2 uppercase and 3 lowercase letters): "))
    new_list = counts_upper_and_lower(text)
