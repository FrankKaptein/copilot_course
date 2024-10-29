import random

def get_user_choice():
    user_input = input("Kies steen, papier of schaar: ").lower()
    while user_input not in ["steen", "papier", "schaar"]:
        user_input = input("Ongeldige keuze. Kies steen, papier of schaar: ").lower()
    return user_input

def get_computer_choice():
    return random.choice(["steen", "papier", "schaar"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Gelijkspel!"
    elif (user_choice == "steen" and computer_choice == "schaar") or \
         (user_choice == "papier" and computer_choice == "steen") or \
         (user_choice == "schaar" and computer_choice == "papier"):
        return "Jij wint!"
    else:
        return "Computer wint!"

def play_game():
    user_score = 0
    computer_score = 0
    rounds = int(input("Hoeveel rondes wil je spelen? "))
    
    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Jij koos: {user_choice}")
        print(f"Computer koos: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "Jij wint!":
            user_score += 1
        elif result == "Computer wint!":
            computer_score += 1
    
    print(f"Eindscore - Jij: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("Gefeliciteerd! Je hebt gewonnen!")
    elif user_score < computer_score:
        print("Helaas, de computer heeft gewonnen.")
    else:
        print("Het is een gelijkspel!")

if __name__ == "__main__":
    play_game()