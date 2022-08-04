quote = "keep looking up"

print("You have to guess this quote: ", end="")
for letter in quote:
    if letter != " ":
        print("#", end="")
    else:
        print(" ", end="")
print("")
guess_quote = str(input("Guess a letter or press / if you think you know the quote: "))
quote_data = []

while guess_quote != "/":
    counter = 0
    
    print("You already have this result: ", end="")
    for letter in quote:
        if guess_quote == letter:
            print(guess_quote, end="")
            quote_data.append(guess_quote)
        elif letter in quote_data:
            print(letter, end="")
        elif letter == " ":
            print(" ", end="")
        else:
            print("#", end="")
        counter += 1
    print("")

    guess_quote = str(input("Guess another letter: "))

know_the_word = str(input("OK. You think you know, just say it. ")).lower()

if know_the_word == quote:
    print("Yes, you win!")
else:
    print("Sorry, wrong quote")
