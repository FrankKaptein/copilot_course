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
    print('q: Quit')
        
    # Get and validate user input
    user_input = input('Enter your choice: ').strip().lower()
    while not is_valid_input(user_input):
        user_input = input('Invalid choice. Enter your choice: ').strip().lower()
    
    # Convert number input to corresponding game option
    if user_input.isdigit():
        user_input = game_options[int(user_input)]
    
    return user_input

# Define function to validate user input
def is_valid_input(user_input):
    # Check if input is 'q' to quit
    if user_input == 'q':
        return True
    # Check if input is a valid game option number
    if user_input.isdigit() and int(user_input) in game_options.keys():
        return True
    # Check if input is a valid game option name
    if user_input in game_options.values():
        return True
    return False

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
    user_score = 0
    computer_score = 0
    while True:
        # Get user input
        user_choice = get_user_input()
        if user_choice == 'q':
            print('Thanks for playing!')
            print(f'Final Score - You: {user_score}, Computer: {computer_score}')
            break
        # Get computer input
        computer_choice = get_computer_input()
        # Determine game result
        game_result = get_game_result(user_choice, computer_choice)
        # Update scores
        if game_result == game_results['win']:
            user_score += 1
        elif game_result == game_results['lose']:
            computer_score += 1
        # Display game result
        print(f'User choice: {user_choice}')
        print(f'Computer choice: {computer_choice}')
        print(f'Game result: {game_result}')
        print(f'Score - You: {user_score}, Computer: {computer_score}')

# Call main function
if __name__ == '__main__':
    main()
