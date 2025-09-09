import random


def get_choices():
    player_choice = input(
        "Enter your choice (rock, paper, scissors): ").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


choices = get_choices()
print(choices)


# food = ["pizza", "carrots", "eggs"]
# dinner = random.choice(food)

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors"):
        return "You win!"
    elif (player == "paper" and computer == "rock"):
        return "You win!"
    elif (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "you lose!"


print(check_win(choices["player"], choices["computer"]))
