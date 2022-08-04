three_digit = input("Enter a three-digit number: ")

print("Half =", int(three_digit) / 2)
print("Double =", int(three_digit) * 2)
print("Third power =", int(three_digit) ** 3)
print("Tenfold =", int(three_digit) * 10)
for i in range(len(three_digit)):
    print(three_digit[i])
