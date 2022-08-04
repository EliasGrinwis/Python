word = str(input("Enter a text consisting only of letters and numbers: "))

print("The numbers:")

set_numbers = set()
set_letters = set()

for number in word:
    if number.isdigit():
        set_numbers.add(number)
    else:
        set_letters.add(number)

for number in set_numbers:
    print(number)

print("The letters:")
for letter in set_letters:
    print(letter)
