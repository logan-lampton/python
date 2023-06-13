import art
import random
import os

# Logo for game and array of cards
print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  "Randomly deals a card"
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Takes a list of cards and return the sum of them"""
  if sum (cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, dealer_score):
  """Compare the user and dealer scores as arguments"""
  if user_score == dealer_score:
   return "It's a tie and the dealer wins ties. You lose 🙃"
  elif dealer_score == 0:
    return "OOOF! The dealer got a blackjack 💀"
  elif user_score == 0:
    return "BLACKJACK! You win!!! 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif dealer_score > 21:
    return "Dealer went over! You win 😁"
  elif user_score > dealer_score:
    return "You're closer to 21! You win 😁"
  else:
    return "The dealer's score is closer to 21. You lose 😭"
   
def blackjack():
  """Runs a blackjack game"""
  begin_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if begin_choice == 'y':
    os.system('clear')
    print(art.logo)
    user_hand = []
    dealer_hand = []
    game_continues = True
    # intial deal
    for _ in range(2):
      user_hand.append(deal_card())
      dealer_hand.append(deal_card())
    while game_continues:
      # calculate scores
      user_score = calculate_score(user_hand)
      dealer_score = calculate_score(dealer_hand)
      # print scores
      print(f"Your cards: {user_hand}; current score: {user_score}")
      print(f"The dealer's first card is: {dealer_hand[0]}.")
      print("The closest to 21 without going over wins.")
      # ask if play wants to continue/logic to end the game
      if user_score == 0 or dealer_score == 0 or user_score > 21:
        game_continues = False
      else:
        whether_to_draw_again = input("Would you like to draw another card? Type 'y' or 'n': ").lower()
        if whether_to_draw_again == 'y':
          os.system('clear')
          print(art.logo)
          user_hand.append(deal_card())
          user_score = calculate_score(user_hand)
        else:
          game_continues = False
      while dealer_score <= 21 and dealer_score < user_score and user_score <= 21:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)
      # Comparing scores/final screen
    os.system('clear')
    print(art.logo)
    print(f"Your final hand: {user_hand}; final score: {user_score}")
    print(f"The dealer's final hand: { dealer_hand}; final score: {dealer_score}")
    print(compare(user_score, dealer_score))
    # recursive call
    blackjack()
  # If they opt to not play
  else:
       print("Okay, bye!") 

# Inital call
blackjack()