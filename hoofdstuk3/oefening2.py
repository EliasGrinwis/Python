number = input("Enter a number: ")
sixes = 0
zeros = 0

for i in range(len(number)):
    if number[i] == "6":
        sixes += 1
    if number[i] == "0":
        zeros += 1
    
print("The number consists of", zeros, "zeros and", sixes, "sixes")
