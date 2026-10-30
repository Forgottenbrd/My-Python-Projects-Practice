import random
the_number = random.randint(1, 100)

attempts = 0
while True:
    input_number = int(input("Guess the number (between 1 and 100): "))
    attempts+=1

    if the_number < input_number:
        print("Too high!")
    elif the_number > input_number:
        print("Too low!")
    elif the_number == input_number:
        print(f"Congratulation! The number was {the_number}\nYou have guessed the number in {attempts} attempts")
        break

