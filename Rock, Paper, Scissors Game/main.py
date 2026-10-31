
import random

while True:
    player_chose = input("rock, paper, or scissors? (r/p/s): ")

    options = ["r","p","s"]

    computer_chose = random.choice(options)

    print(f"You chose {player_chose}")
    print(f"Computer chose {computer_chose}")

    player_win = [("r","s"), ("p","r"),("s","p")]

    if player_chose == computer_chose:
        print("It is a draw")
    elif (player_chose, computer_chose) in player_win: 
        print("You win!!!")
    else:
        print("You lose")




# r == "🪨"
# p == "📄"
# s == "✂️"

