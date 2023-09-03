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
images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(images[user_choice])

computer_choice = random.randint(0,2)
print(images[computer_choice])

# the more important stament must be at the top
if user_choice >= 3 or user_choice < 0:
  print("Type a number bewteen 0 and 2. Try again")
# the more important stament must be at the top
else:
# the more important stament must be at the top
  if computer_choice == 0 and user_choice == 2:
    print("You lose")
# the more important stament must be at the top
  if user_choice == 0 and computer_choice == 2:
    print("You win")
  elif user_choice > computer_choice:
    print("You win")
  elif computer_choice == user_choice:
    print("It's a draw")
  elif user_choice < computer_choice:
    print("You lose")    