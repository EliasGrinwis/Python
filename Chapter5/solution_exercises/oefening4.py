numbers = (1, 2, 3, 4, 5, 6, 7, 8)
print(numbers)

index1 = numbers.index(4)

for number in numbers:
    if number == index1:
        print(numbers[index1 + 1 : ])
