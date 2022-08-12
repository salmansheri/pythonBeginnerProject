import random

userWins = 0
computerWins = 0
options = ["rock", "paper", "scissors"]

while True:
    userInput = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if userInput == "q":
        break

    if userInput not in options:
        continue

    randomNumber = random.randint(0, 2)
    # rock: 0, paper: 1, scissor: 2
    computer_pick = options[randomNumber]
    print("Computer Picked {}".format(computer_pick + "."))

    if userInput == "rock" and computer_pick == "scissors":
        print(" You won!")
        userWins += 1
        continue

    elif userInput == "paper" and "rock":
        print("You Win!")
        userWins += 1

    elif userInput == "scissors" and computer_pick == "paper":
        print("You won!")
        userWins += 1

    else:
        print("You Lost!")
        computerWins += 1

print("You won {} times".format(userWins))
print("The computer won {}".format(computerWins))

print("Goodbye!")
