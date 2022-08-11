def encode_a_list_of_words():
    original_list = ["yellow", "green", "blue", "purple"]
    encoded_list = []

    start_value = ord('e')
    minimum_value = ord('a')
    end_value = ord('z')
    print(minimum_value)
    print(end_value)

    for letter in original_list:
        #print(letter)
        one_word_string = ""
        for single_letter in letter:

            single_letter_new = start_value - ord(single_letter)  # 101   -  #100
            new_value = start_value + single_letter_new
            if new_value < minimum_value:
                change_value = 97 - new_value
                newest_value = 123 - change_value

                one_word_string += chr(newest_value)

                #print(one_word_string)
                #print(chr(newest_value))

            else:
                one_word_string += chr(new_value)
                #print(chr(new_value))

        encoded_list.append(one_word_string)

    print("original: ", original_list)
    print("encoded: ", encoded_list)


encode_a_list_of_words()
