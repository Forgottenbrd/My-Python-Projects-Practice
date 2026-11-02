import random

# Fixed values
OPTIONS = ["r","p","s"]
WINNING_RULES = [("r","s"), ("p","r"),("s","p")]
EMOJIS = {"r": "🪨", "p": "📄", "s": "✂️"}
# name of players
name1 = "Player"
name2 = "Computer"


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
def show_the_round(the_winning_number, name1, choice1, name2, choice2):
    '''It takes the_winning_number, name1, choice1, name2, choice2 and decide the winner and prints everything.
    '''
    print(f"{name1} chose {EMOJIS[choice1]}")
    print(f"{name2} chose {EMOJIS[choice2]}")
    if the_winning_number == "PLAYER1_WINS":
        print(f"The winner is {name1}")
    elif the_winning_number == "PLAYER2_WINS":
        print(f"The winner is {name2}")
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
def main():
    playing = True
    while playing:
        choice1 = get_player_choice()
        choice2 = get_computer_choice()
        the_winning_number = decide_the_winner(choice1, choice2)
        show_the_round(the_winning_number, name1, choice1, name2, choice2)
        playing = replay()

if __name__ == "__main__":
    main()