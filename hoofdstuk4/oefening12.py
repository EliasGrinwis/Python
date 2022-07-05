word = str(input("Enter a string: "))

previous_letter = word[0]
new_word = ""


for letter in word:
    if letter == "*":
        new_word.replace(previous_letter, "")

    previous_letter = letter
    new_word += previous_letter

print(new_word)

#NEED TO FIX THIS   