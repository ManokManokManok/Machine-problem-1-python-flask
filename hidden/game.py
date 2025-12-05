import random

def get_computer_choice():
    """Get a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    """Determine the winner of the game."""
    if player_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combinations[player_choice] == computer_choice:
        return "player"
    else:
        return "computer"

def play_game():
    """Main game loop."""
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        player_choice = input("\nEnter your choice (rock/paper/scissors) or 'quit' to exit: ").lower()
        
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        
        if result == "tie":
            print("It's a tie!")
        elif result == "player":
            print("You win!")
        else:
            print("Computer wins!")

if __name__ == "__main__":
    play_game()