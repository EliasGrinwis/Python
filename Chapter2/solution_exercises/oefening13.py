import random

rock_papers_scissors = ["rock", "paper", "scissors"]
computer_choice = rock_papers_scissors[random.randint(0, 2)]

player_choice = str(input("What do you choose: paper, rock or scissors? ")).lower()
print("You chose", player_choice)
print("I chose", computer_choice)

#rock > scissors     scissors > paper        paper > rock

#CHECK WHO WIN
if player_choice == "rock" and computer_choice == "scissors":
    print("You win :-)")
elif player_choice == "scissors" and computer_choice == "paper":
    print("You win :-)")
elif player_choice == "paper" and computer_choice == "rock":
    print("You win :-)")
else:
    print("You lose")
