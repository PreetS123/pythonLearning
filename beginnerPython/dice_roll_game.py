import random

rolls = int(input("How many times do you want to roll the dice? "))

num_dice= int(input("How many dice do you want to roll each time? "))
for i in range(rolls):

     option= input(f"Roll {num_dice} (y/n) ").lower()

     if option=='y':
         dice_value=[random.randint(1,6) for _ in range(num_dice)]
         print('You rolled:',",".join(map(str,dice_value)))
     elif option=='n':
         print("Thanks for playing!")
     else:
         print("Invalid option")