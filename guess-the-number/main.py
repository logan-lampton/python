#Number Guessing Game Objectives:

# Include an ASCII art logo.
import art
import random
import os

def guess_the_number():
  """Number guessing game generating a number from 1 to 100. No arguments"""
  os.system('clear')
  print(art.logo)
  # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
  difficulty_mode = input("Please choice your difficulty mode: 'easy' or 'hard': ").lower()
  
  if difficulty_mode == "easy":
    guesses_remaining = 10
  else:
    guesses_remaining = 5
  
  answer = random.randint(1, 101)

  def play_again():
    """Presents option to play the game again/restarts the game. No arguments"""
    choice = input("Would you like to play again? Type 'y' or 'n': ").lower()
    if choice == "y":
      guess_the_number()
    else:
      print("Goodbye")
  
  # Allow the player to submit a guess for a number between 1 and 100.
    # Check user's guess against actual answer. Print "Too high." or       "Too low." depending on the user's answer. 
    # If they got the answer correct, show the actual answer to the         player.
  
  def guess():
    """Function to handle player guessing the number. No arguments"""
    player_guess = int(input("Guess a number between '1' and '100': "))
    if player_guess == answer:
      print(f"You win! The correct number is {answer}")
      play_again()
    elif player_guess > answer:
      print("Too high.")
    else:
      print("Too low.")
    # # For my testing
    # print(f"Player guess: {player_guess}")
    # print(f"The answer: {answer}")
  
  guess()
  
  while guesses_remaining > 0:
    # Track the number of turns remaining.
    guesses_remaining -= 1
    if guesses_remaining > 0:
      print(f"You have {guesses_remaining} guesses left. Guess again")
      guess()
    # If they run out of turns, provide feedback to the player.
    else:
      print("No guesses left. You lose.")
      play_again()
    
guess_the_number()
