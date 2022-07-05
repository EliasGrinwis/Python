text = str(input("Enter a text: "))

new_list = []

for letter in text:
    if letter != " ":
        new_list.append(letter)

print(new_list)

print("")

for letter in new_list:
    print(letter, end=" ")

print("")
print("")

print(*[letter for letter in new_list], sep="   ")

