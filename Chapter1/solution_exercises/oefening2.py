yes_votes = int(input("How many people voted YES: "))
no_votes = int(input("How many people voted NO: "))
blank_votes = int(input("Number of blank votes: "))

print("YES:", str((yes_votes / (yes_votes + no_votes + blank_votes)) * 100) + "%")
print("NO:", str((no_votes / (yes_votes + no_votes + blank_votes)) * 100) + "%")
print("Blank:", str((blank_votes / (yes_votes + no_votes + blank_votes)) * 100) + "%")
