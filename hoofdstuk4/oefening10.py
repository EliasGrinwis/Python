counter = 0

word_list = []

while counter != 5:
    counter += 1
    word = str(input("Enter a word " + str(counter) + ": "))
    word_list.append(word)

print("The words in reverse order:")
print(word_list[-1].capitalize(), word_list[-2].capitalize(), word_list[-3].capitalize(), word_list[-4].capitalize(), word_list[-5].capitalize())
