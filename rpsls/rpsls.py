# TODO: Develop a console-based Rock Paper Scissors Lizard Spock game in Python
# Game should be modular, allowing for easy updates or rule changes
# Implement game rules:
# - Scissors decapitate lizard
# - Scissors cuts paper
# - Paper covers rock 
# - Rock crushes lizard 
# - Lizard poisons Spock 
# - Spock smashes scissors 
# - Lizard eats paper 
# - Paper disproves Spock 
# - Spock vaporizes rock 
# - Rock crushes scissors
# Include user input for selecting options and display game results

import random

# Define global variables
# Define dictionary of game options
game_options = {
    1: 'rock',
    2: 'paper',
    3: 'scissors',
    4: 'lizard',
    5: 'spock'
}

# Define dictionary for game rules
game_rules = {
    'rock': ['lizard', 'scissors'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['spock', 'paper'],
    'spock': ['scissors', 'rock']
}

# Define dictionary for game results
game_results = {
    'win': 'You win!',
    'lose': 'You lose!',
    'draw': 'It\'s a draw!'
}

# Define function to get user input
def get_user_input():
    # Display game options
    print('Game Options:')
    for key, value in game_options.items():
        print(f'{key}: {value}')
    # Get user input
    user_input = int(input('Enter your choice: '))
    # Validate user input
    while user_input not in game_options.keys():
        user_input = int(input('Invalid choice. Enter your choice: '))
    return game_options[user_input]

# Define function to get computer input
def get_computer_input():
    return random.choice(list(game_options.values()))

# Define function to determine game result
def get_game_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return game_results['draw']
    elif computer_choice in game_rules[user_choice]:
        return game_results['win']
    else:
        return game_results['lose']
    
# Define main function
def main():
    # Get user input
    user_choice = get_user_input()
    # Get computer input
    computer_choice = get_computer_input()
    # Determine game result
    game_result = get_game_result(user_choice, computer_choice)
    # Display game result
    print(f'User choice: {user_choice}')
    print(f'Computer choice: {computer_choice}')
    print(f'Game result: {game_result}')

# Call main function
if __name__ == '__main__':
    main()
