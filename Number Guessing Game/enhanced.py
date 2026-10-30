import random

attempts = 0

print("Welcome! to my guessing game!")

max_number = int(input("Enter the maximum value: "))
min_number = int(input("Enter the minimum value: "))
the_number = random.randint(min_number, max_number)

while True:
    attempts+=1
    input_number = int(input(f"Guess the number (between {min_number} and {max_number}): "))
    if the_number < input_number:
        print("Too high! Try again!")
    elif the_number > input_number:
        print("Too low! Try again!")
    elif the_number == input_number:
        print(f"Congratulation! The number was {the_number}\nYou have guessed the number in {attempts} attempts")
        break

