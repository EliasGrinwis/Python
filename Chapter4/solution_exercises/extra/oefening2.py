#0 --> 3
alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

not_encrypted_text = str(input("Enter the text to be encrypted: "))
encrypted_text = ""
number_of_characters = int(input("Enter the number of characters you want to rotate with: "))

counter = 0

for letter in not_encrypted_text:

    if letter == " ":
        encrypted_text += "#"
    else:
        if (alpabet.index(letter) + number_of_characters) > 50:
            print(alpabet.index(letter) + number_of_characters)
            #encrypted_text += alpabet[alpabet.index(letter) + number_of_characters - 50]
        elif (alpabet.index(letter) + number_of_characters > 25):
            encrypted_text += alpabet[alpabet.index(letter) + number_of_characters - 26]
        else:
            encrypted_text += alpabet[alpabet.index(letter) + number_of_characters]


print(encrypted_text)

#Need to fix this
