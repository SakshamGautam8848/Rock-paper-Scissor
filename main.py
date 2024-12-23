import random

print("Welcome to the Rock Paper Scissor Game")

user_wins = 0
computer_wins = 0
tie = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    if user_input =="q":
        break

    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    # rock: 0 , paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("COmputer picked", computer_pick + ".")

    # Check if it's a tie
    if user_input == computer_pick:
        print("It's a tie")
        tie += 1
        continue

    # Check if the user wins
    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
        continue
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
        continue
    
    else:
        print("You Lost!")
        computer_wins += 1



print("You won", user_wins, "times")
print("The computer", computer_wins, "times")
print("The game tied", tie, "times")
print("Goodbye!")
