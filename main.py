import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))  # what the user chose when they typed in a value

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number. You lose.")  # sequence matters. the code will be checked in order; from top to bottom
else:
  print(game_images[user_choice])
  
  computer_choice = random.randint(0, 2)  # we'll generate a random number for the computer choice. To do this, we will import the random module
                    # what's inside the range() is basically the start (before comma) and stop (after comma; where it starts and ends its selection
  
  print("Computer chose: ")  # remember to test as you go
  print(game_images[computer_choice])
  
  
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win")
  elif computer_choice == user_choice:
    print("It's a draw")
