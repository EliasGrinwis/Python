text = str(input("Enter a text: "))

counter = 0
previous_letter = text[0]
highest_block = 0

for letter in text:
    if letter == previous_letter:
        counter += 1
        if counter >= highest_block:
            highest_block = counter
    else:
        counter = 1
    previous_letter = letter

print("The length of the largest block in this text is", highest_block)
