word = str(input("Enter a word: "))

if word[::-1] == word:
    print("This is a palindrome")
else:
    print(word, "is not a palindrome")
