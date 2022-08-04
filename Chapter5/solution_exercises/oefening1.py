original_list = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]

print("Original list: \t", original_list)

new_list = original_list

first_word = original_list[0]
last_word = original_list[-1]

new_list.remove(original_list[0])
new_list.remove(original_list[-1])

new_list.insert(0, last_word)
new_list.append(first_word)

print("After the switch: ", new_list)
