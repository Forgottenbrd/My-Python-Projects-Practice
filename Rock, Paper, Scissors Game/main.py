import random
from getpass import getpass

# Fixed values
OPTIONS = ["r","p","s"]
WINNING_RULES = [("r","s"), ("p","r"),("s","p")]
EMOJIS = {"r": "🪨", "p": "📄", "s": "✂️"}
SOLO = "solo"
DUEL = "duel"
TITLE = "Adventurer"

TEXT = {
    "greeting": "[CORE] A new presence has crossed the Gate.\n"
                "I am the Core. I guard the path to the next stage.\n"
                "Only the worthy may pass. Let us see what you are, {title}.",
    "menu_title": "[CORE] Choose your trial, {title}:",
    "mode_prompt": "Your trial (1/2/3): ",
    "mode_error": "[CORE] That is not a trial I offer. Choose 1, 2 or 3.",
    "choice_prompt": "Rock, paper, or scissors? (r/p/s): ",
    "choice_error": "[CORE] Invalid move. I accept only {options}.",
    "chose": "{name} chose {emoji}",
    "round_start": "--- Round {number} ---",
    "round_win": "[CORE] {name} takes this round.",
    "round_draw": "[CORE] Neither of us prevails. A draw.",
    "match_win": "[CORE] You have proven yourself, {title}. The path to the next stage opens.",
    "match_lose": "[CORE] You are not yet worthy. The Gate remains closed.",
    "match_draw": "[CORE] A deadlock. I do not pass the undecided.",
    "sealed": "[CORE] I have already won two rounds. You may still play the third.",
    "replay_prompt": "Face me again? (y/n): ",
    "replay_error": "[CORE] Answer with y or n.",
    "practice_intro": "[CORE] The Training Hall opens, {title}s. I will only watch. Sharpen yourselves against each other.",
    "duel_turn": "[CORE] {name}, step forward and choose.",
    "duel_hide": "[CORE] {other}, avert your eyes.",
    "duel_draw": "[CORE] Neither {title} prevails. A draw.",
    "duel_replay_prompt": "Another duel? (y/n): ",
    "duel_end": "[CORE] The Training Hall closes. Return when you are ready for the real trial.",
}

GAME_MODES = {
    "1": "Single Trial - one round against me",
    "2": "Gate Trial - three rounds; win the most to pass",
    "3": "Training Hall - practice against another adventurer",
}

name1 = TITLE
name2 = "The Core"


def greeting():
    the_line(62)
    print(TEXT["greeting"].format(title=TITLE))
def get_game_mode():
    '''Asking the Game mode.
    Returning the the game mode number.
    '''
    the_line(62)
    print(TEXT["menu_title"].format(title=TITLE))
    for key, game_mode in GAME_MODES.items():
        print(f"{key}) {game_mode}")
    asking = True
    while asking:
        game_mode = input(TEXT["mode_prompt"]).strip()
        if game_mode in GAME_MODES:
            asking = False
        else:
            print(TEXT["mode_error"])
    return game_mode
def get_player_choice(hidden=False):
        """Ask for a move until the player enters a valid one.

        Args:
            hidden: If True, the typing is not shown on screen, so a
                rival cannot peek (used in the Training Hall).

        Returns:
            str: One of the moves in OPTIONS, in lower case.
        """
        
        if hidden:
            input_method = getpass
        else:
            input_method = input
        
        while True:
            player_choice = input_method(TEXT["choice_prompt"]).lower().strip()
            if player_choice in OPTIONS:
                break
            else:
                print(TEXT["choice_error"].format(options=", ".join(OPTIONS)))
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
def show_the_round(the_winner, name1, choice1, name2, choice2, mode=SOLO): # Take note
    '''It takes the_winning_number, name1, choice1, name2, choice2 and decide the winner and prints everything.
    '''
    print(TEXT["chose"].format(name=name1, emoji=EMOJIS[choice1])) # Take note
    print(TEXT["chose"].format(name=name2, emoji=EMOJIS[choice2])) 

    # Winning logic
    if the_winner == "PLAYER1_WINS":
        print(TEXT["round_win"].format(name=name1))
    elif the_winner == "PLAYER2_WINS":
        print(TEXT["round_win"].format(name=name2))
    else:
        if mode == "duel":
            print(TEXT["duel_draw"].format(title=TITLE))
        else:
            print(TEXT["round_draw"])
def replay(mode=SOLO):
    '''It ask the user for replay. output True or False for main() loop.
    '''
    while True:
        if mode == DUEL:
            prompt = TEXT["duel_replay_prompt"]
        else:
            prompt = TEXT["replay_prompt"]
        again = (input(prompt)).lower()
        if again == "y":
            result = True
            break
        elif again == "n":
            result = False
            break
        else:
            print(TEXT["replay_error"])
    return result
def the_line(length=40):
    print("=" * length)

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
        while round_number < 3:
            round_number += 1
            the_line()
            print(TEXT["round_start"].format(number=round_number))
            choice1 = get_player_choice()
            choice2 = get_computer_choice()
            the_winner = decide_the_winner(choice1, choice2)
            scores[the_winner] += 1
            show_the_round(the_winner, name1, choice1, name2, choice2)
            if scores["PLAYER2_WINS"] == 2 and round_number == 2: # Extra
                print(TEXT["sealed"])
        if scores["PLAYER1_WINS"] > scores["PLAYER2_WINS"]:
            the_line()
            print(TEXT["match_win"].format(title=TITLE))
        elif scores["PLAYER2_WINS"] > scores["PLAYER1_WINS"]:
            the_line()
            print(TEXT["match_lose"])
        else:
            the_line()
            print(TEXT["match_draw"])
        
        
    elif game_mode == "3":
        duelist1 = f"{TITLE} 1"
        duelist2 = f"{TITLE} 2"
        the_line()
        print(TEXT["practice_intro"].format(title = TITLE))
        the_line()
        playing = True
        while playing:    
            print(TEXT["duel_turn"].format(name=duelist1))
            choice1 = get_player_choice(hidden=True)
            the_line()
            print(TEXT["duel_hide"].format(other=duelist2))
            the_line()
            print(TEXT["duel_turn"].format(name=duelist2))
            choice2 = get_player_choice(hidden=True)
            the_line()
            the_winner = decide_the_winner(choice1, choice2)
            show_the_round(the_winner, duelist1, choice1, duelist2, choice2, mode=DUEL)
            playing = replay(mode=DUEL)



if __name__ == "__main__":
    main()