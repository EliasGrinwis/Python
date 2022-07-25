animal_sounds = {"horse": "neigh", "cat": "meows", "dog": "barks", "cow": "mooing"}

print("Do you know the animal sounds?")

correct_answer = 0

for animal in animal_sounds:
    animal_input = input("What is the sound of a " + animal + ": ")

    if animal_input == animal_sounds[animal]:
        correct_answer += 1

print("You have", correct_answer, "correct answers.")
