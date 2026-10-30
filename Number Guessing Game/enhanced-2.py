import random


# Greeting
print("Welcome! to my guessing game!")

# inputs
while True:
    try:
        max_number = int(input("Enter the maximum value: "))
        min_number = int(input("Enter the minimum value: "))
        max_attempts = int(input("Enter the max attempts for the game: "))
        break
    except:
        print("Please enter the right number!")
        
attempts = 0
# Number selection
the_number = random.randint(min_number, max_number)

while True:
    try:
        input_number = int(input(f"Guess the number (between {min_number} and {max_number}): "))
    except:
        print("Please enter the right number!")
        continue

    attempts+=1
    if max_attempts == attempts:
        print(f"Game Over! The number was {the_number}\nThank you! for plaing my game. Bye :)")
        break
    elif the_number < input_number:
        print("Too high! Try again!")
    elif the_number > input_number:
        print("Too low! Try again!")
    elif the_number == input_number:
        print(f"Congratulation! The number was {the_number}\nYou have guessed the number in {attempts} attempts")
        break
