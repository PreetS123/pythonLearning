import random


"""
Generate a random number
Ask the user to make a guess
If not a valid number
  Print an error
  if number< guess
    Print too low
    If number>guess 
    Print too high
"""



num_generated = random.randint(1,100)

while True:
    guessed= input("Guess the number (1-100): ")

    if not guessed.isdigit():  
        print("Not a valid number")
        continue
    else:
          num_guessed= int(guessed)
          if int(num_guessed) < num_generated:  
              print("Too low")
          elif int(num_guessed) > num_generated:  
             print("Too high")
          elif int(num_guessed) ==num_generated:
              print("Correct")
              break
          else:
              print("Something went wrong!")
              break