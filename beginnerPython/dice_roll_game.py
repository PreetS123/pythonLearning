import random

option= input("Roll the dice? (y/n)").lower()

if option=='y':
    dice1=random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f'{dice1}, {dice2}')
elif option=='n':
    print("Thanks for playing!")
else:
    print("Invalid option")