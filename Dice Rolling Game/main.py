import random

roll_counter=0
while True:
    try:
        roll_count = int(input("How many Dice Roll do you want?: "))
        result=[]
        
        for r in range(roll_count):
            result.append(random.randint(1,6))
            roll_counter+=1
        print(result)

        print(f"You have rolled the dice {roll_counter} times in this session")
        repeat = input("Roll the dice again? (y/n): ").lower()

        # Break logic
        if repeat == "n":
            break
        
    except:
        print("Invalid Input!!")
