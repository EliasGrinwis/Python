text = str(input("Enter a text: "))

counter = 0
triple = 0
previous_letter = ""

for letter in text:
    if letter == previous_letter:
        counter += 1
        if counter >= 2:
            triple += 1
    else:
        counter = 0
    previous_letter = letter

if triple == 0:
    print("There are no triples in this text")
elif triple == 1:
    print("There is", triple, "triple in this text")
else:
    print("There are", triple, "triples in this text")
