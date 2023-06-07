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

print("Rock, Paper, Scissors time!")

# Player Choice
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
if player_choice == 0:
  print(f"You chose: Rock! {rock}")
elif player_choice == 1:
  print(f"You chose: Paper! {paper}")
elif player_choice == 2:
  print(f"You chose: Scissors! {scissors}")
else:
  print("Please choose 0, 1, or 2")

# Random Computer Choice
computer_choice = random.randint(0, 2)
if computer_choice == 0:
  print(f"The Computer chose: Rock! {rock}")
elif computer_choice == 1:
  print(f"The Computer chose: Paper! {paper}")
elif computer_choice == 2:
  print(f"The Computer chose: Scissors! {scissors}")

# Select Winner
if player_choice == 0:
  if computer_choice == 0:
    print("It's a tie!")
  elif computer_choice == 1:
    print("Dun! Dun! Dun! You lose!")
  elif computer_choice == 2:
    print("You win!!!")
elif player_choice == 1:
  if computer_choice == 0:
    print("You win!!!")
  elif computer_choice == 1:
    print("It's a tie!")
  elif computer_choice == 2:
    print("Dun! Dun! Dun! You lose!")
elif player_choice == 2:
  if computer_choice == 0:
    print("Dun! Dun! Dun! You lose!")
  elif computer_choice == 1:
    print("You win!!!")
  elif computer_choice == 2:
    print("It's a tie!")

print("Thanks for playing, feel free to play again!")