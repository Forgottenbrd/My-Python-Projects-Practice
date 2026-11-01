
import random
# Input!!!----------------------------------------------------------------------------------------------------
# Main loop

while True:
    # Input loop
    while True:
        try:
            # Input
            player_chose = input("rock, paper, or scissors? (r/p/s): ").lower()
            options = ["r","p","s"]

            computer_chose = random.choice(options)
            # Error check
            if player_chose in options:
                break
            else:
                raise ValueError
        except:
            print(f"Only choose from {options} ")

# Logic!!!----------------------------------------------------------------------------------------------------
    # winning conditions
    player_win = [("r","s"), ("p","r"),("s","p")]

    # Winning logic
    if player_chose == computer_chose:
        the_result = ("It is a draw")
    elif (player_chose, computer_chose) in player_win: 
        the_result = ("You win!!!")
    else:
        the_result = ("You lose")

    emojis = {"r": "🪨", "p": "📄", "s": "✂️"}

# Show!!!----------------------------------------------------------------------------------------------------
    # Chose show
    print(f"You chose {emojis[player_chose]}")
    print(f"Computer chose {emojis[computer_chose]}")
    print(the_result)

# Repaly!!!----------------------------------------------------------------------------------------------------
    # Mian loop break
    while True:
        again = (input("Continue? (y/n): ")).lower()

        if again in ("y","n"):
            break
        else: 
            print("Please enter only (y/n)")

    if again == "n":
        break
    else:
        pass