import random
# Input!!!----------------------------------------------------------------------------------------------------

# Fixed values
OPTIONS = ["r","p","s"]
WINNING_RULES = [("r","s"), ("p","r"),("s","p")]
EMOJIS = {"r": "🪨", "p": "📄", "s": "✂️"}
PLAYER1_WINS = 1
PLAYER2_WINS = 2
DRAW = 0
# name of players
name1 = "Player"
name2 = "Computer"


def get_player_choice():
        '''Getting the input from the player and matching it against the "option" variable.
        else, asking to chose from option agin.

        Returns - One of the valid options in lower case.
        '''
        while True:
            player_choice = input("rock, paper, or scissors? (r/p/s): ").lower()

            if player_choice in OPTIONS:
                break
            else:
                print(f"Only choose from {OPTIONS} ")

        return player_choice
def get_computer_choice():
    '''This function chosing a random choice from options and returns it.
    '''
    computer_choice = random.choice(OPTIONS)
    return computer_choice
def decide_the_winner(choice1, choice2):
    '''It takes choice1, choice2 choice and compare it against WINNING_RULES.
    It returns 1 for choice1 win, 2 for choice2 win, 0 for draw.
    '''
    if choice1 == choice2:
        the_result = 0
    elif (choice1,choice2) in WINNING_RULES:
        the_result = 1
    else:
        the_result = 2
    return the_result
def show_the_round(the_winning_number, name1, choice1, name2, choice2):
    '''It takes the_winning_number, name1, choice1, name2, choice2 and decide the winner and prints everything.
    '''
    print(f"{name1} chose {EMOJIS[choice1]}")
    print(f"{name2} chose {EMOJIS[choice2]}")
    if the_winning_number == 1:
        print(f"The winner is {name1}")
    elif the_winning_number == 2:
        print(f"The winner is {name2}")
    else:
        print("It is a draw!")
def replay():
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