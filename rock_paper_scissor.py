import random

print("Welcome to Rock, Paper, Scissors!")

# Get player's choice
player = input("1 is for '✊' (Rock).\n2 is for '✋' (Paper).\n" \
"3 is for '✌️' (Scissors). \n" \
"Please enter a number: ")

# Validate player's input
if player == '1':
    player = '✊'
elif player == '2':
    player = '✋'
elif player == '3':
    player = '✌️'
else:
    print("Invalid input. Please enter 1, 2, or 3.")
    exit()

# Generate computer's choice
computer_num = random.randint(1, 3)
if computer_num == 1:
    computer = '✊'
elif computer_num == 2:
    computer = '✋'
else:
    computer = '✌️'

# Show the choices
print(f"You chose: {player}")
print(f"Computer chose: {computer}")

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == '✊' and computer_choice == '✌️') or
        (player_choice == '✋' and computer_choice == '✊') or
        (player_choice == '✌️' and computer_choice == '✋')
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Show who won
result = determine_winner(player, computer)
print(result)