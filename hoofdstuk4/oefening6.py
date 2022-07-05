word = str(input("Enter a string: "))

counter = 0
new_word = ""
count_the_length = 0

for letter in word:
    count_the_length += 1
    counter += 1
    new_word += letter
    if counter == 3:
        print(new_word[1] + new_word[2] + new_word[0], end="")
        new_word = ""
        counter = 0
    if count_the_length == len(word) and counter == 1:
        print(new_word[0], end=" ")
    if count_the_length == len(word) and counter == 2:
        print(new_word[0] + new_word[1], end=" ")

