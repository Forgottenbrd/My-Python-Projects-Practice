import random

# Fixed values
OPTIONS = ["r","p","s"]
WINNING_RULES = [("r","s"), ("p","r"),("s","p")]
EMOJIS = {"r": "🪨", "p": "📄", "s": "✂️"}
GAME_MODES = {
    "1": "Classic - one round at a time",
    "2": "Best of Three - first to win two rounds",
    "3": "Two Players - challenge a friend",
}
# name of players
name1 = "Player"
name2 = "Computer"


def greeting():
    print("Welcome! to my Rock, Paper, Scissors game!\nPlease enjoy your time here!")
def get_game_mode():
    '''Asking the Game mode.
    Returning the the game mode number.
    '''
    print("=" * 40)
    print("Choose your game mode:")
    for key, game_mode in GAME_MODES.items():
        print(f"{key}) {game_mode}")
    asking = True
    while asking:
        game_mode = input("Enter your mode (1/2/3): ").strip()
        if game_mode in GAME_MODES:
            asking = False
        else:
            print("Please choose 1, 2 or 3.")
    return game_mode
def get_player_choice():
        '''Getting the input from the player and matching it against the "OPTIONS" variable.
        else, asking to chose from option agin.

        Returns - One of the valid options in lower case.
        '''
        while True:
            player_choice = input("rock, paper, or scissors? (r/p/s): ").lower().strip()

            if player_choice in OPTIONS:
                break
            else:
                print(f"Only choose from {OPTIONS} ")

        return player_choice
def get_computer_choice():
    '''This function chosing a random choice from "OPTIONS" and returns it.
    '''
    computer_choice = random.choice(OPTIONS)
    return computer_choice
def decide_the_winner(choice1, choice2):
    '''It takes choice1, choice2 and compare it against WINNING_RULES.
    It returns the winner or draw.
    '''
    if choice1 == choice2:
        the_result = "DRAW"
    elif (choice1,choice2) in WINNING_RULES:
        the_result = "PLAYER1_WINS"
    else:
        the_result = "PLAYER2_WINS"
    return the_result
def show_the_round(the_winner, name1, choice1, name2, choice2):
    '''It takes the_winning_number, name1, choice1, name2, choice2 and decide the winner and prints everything.
    '''
    print(f"{name1} chose {EMOJIS[choice1]}")
    print(f"{name2} chose {EMOJIS[choice2]}")
    if the_winner == "PLAYER1_WINS":
        print(f"The winner is {name1}")
    elif the_winner == "PLAYER2_WINS":
        print(f"The winner of this round is {name2}")
    else:
        print("It is a draw!")
def replay():
    '''It ask the user for replay. output True or False for main() loop.
    '''
    while True:
        again = (input("Continue? (y/n): ")).lower()
        if again == "y":
            result = True
            break
        elif again == "n":
            result = False
            break
        else:
            print("Please enter only (y/n)")
    return result
def the_line():
    print("=" * 40)

def main():
    greeting()
    game_mode = get_game_mode()

    if game_mode == "1":
        playing = True
        while playing:
            choice1 = get_player_choice()
            choice2 = get_computer_choice()
            the_winner = decide_the_winner(choice1, choice2)
            show_the_round(the_winner, name1, choice1, name2, choice2)
            playing = replay()

    elif game_mode == "2":
        round_number = 0
        scores = {"PLAYER1_WINS": 0, "PLAYER2_WINS": 0, "DRAW": 0}
        playing = True
        while round_number < 3:
            round_number += 1
            the_line()
            print(f"Round {round_number} Start!")
            choice1 = get_player_choice()
            choice2 = get_computer_choice()
            the_winner = decide_the_winner(choice1, choice2)
            scores[the_winner] += 1
            show_the_round(the_winner, name1, choice1, name2, choice2)
        if scores["PLAYER1_WINS"] > scores["PLAYER2_WINS"]:
            the_line()
            print(f"{name1} has won the match!")
        elif scores["PLAYER2_WINS"] > scores["PLAYER1_WINS"]:
            the_line()
            print(f"{name2} has won the match!")
        else:
            the_line()
            print("The match was a draw!")
        
        
    elif game_mode == "3":
        duelist1 = "Traveler 1"
        duelist2 = "Traveler 2"
        the_line()
        print("Welcome to 2 player game mode.")
        playing = True
        while playing:    
            print(f"{duelist1}: ")
            choice1 = get_player_choice()
            print(f"{duelist2}: ")
            choice2 = get_player_choice()
            the_winner = decide_the_winner(choice1, choice2)
            show_the_round(the_winner, duelist1, choice1, duelist2, choice2)
            playing = replay()



if __name__ == "__main__":
    main()