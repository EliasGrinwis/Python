print("Enter the scores for the test. use -1 if you want to finish")

score = float(input("score: "))
new_list = []

while score != -1.0:
    new_list.append(score)
    score = float(input("score: "))

print("The scores (ordered):", sorted(new_list))
print("The average of these", len(new_list), "scores =", round(sum(new_list) / len(new_list), 2))
