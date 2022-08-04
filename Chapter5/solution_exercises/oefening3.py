original_list = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]
print("Original list: ", original_list)

original_list.append(original_list[0])
original_list.pop(0)

print("After sliding: ", original_list)
