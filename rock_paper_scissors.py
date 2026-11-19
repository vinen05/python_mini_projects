import random

user_win = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_guess = input("Type Rock/Papper/Scissors or Q to quit: ").lower()
    if user_guess.lower() == "q":
        break

    if user_guess not in options:
        print("Incorrect Input! Try Again")
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked",computer_pick + ".")

    if user_guess == "rock" and computer_pick == "scissors":
        print("You Win!")
        user_win += 1

    elif user_guess == "paper" and computer_pick == "rock":
        print("You Win!")
        user_win += 1

    elif user_guess == "scissors" and computer_pick == "paper":
        print("You Win!")
        user_win += 1

    else:
        print("You Lost!")
        computer_wins += 1

print("You Won", user_win, "times")
print("Computer Won", computer_wins, "times")
print("GoodBye!")
