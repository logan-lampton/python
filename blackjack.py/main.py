import art
import random
import os

print(art.logo)

def blackjack():
  start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  if start_game == 'y':
    os.system('clear')
    print(art.logo)
    user_hand = []
    dealer_hand = []
    player_draws = True

    def user_draw():
      card = random.choice(cards)
      if card == 11:
        ace_value = int(input("An Ace! What would you like for it to be worth?: Type 1 or 11 "))
        card = ace_value
      user_hand.append(card)

    def dealer_draw():
      card = random.choice(cards)
      if card == 11 and dealer_score <= 10:
          card = 11
      elif card == 11 and dealer_score > 10:
          card = 1
      else:
        card = card
      dealer_hand.append(card)

    user_draw()
    user_draw()
    user_score = sum(user_hand)
    dealer_score = sum(dealer_hand)
    dealer_draw()
    dealer_draw()

    # Player drawing cards 
    while player_draws:  
      print(f"Your cards: {user_hand}; current score: {user_score}")
      print(f"The dealer's first card is: {dealer_hand[0]}.")
      print("The closest to 21 without going over wins.")
      whether_to_draw_again = input("Would you like to draw another card? Type 'y' or 'n': ").lower()
      if whether_to_draw_again == 'y':
        os.system('clear')
        print(art.logo)
        user_draw()
        user_score = sum(user_hand)
        if user_score > 21:
          player_draws = False
      else:
        player_draws = False
        
    # # Dealer drawing cards
    dealer_score = sum(dealer_hand)
    while dealer_score <= 21 and dealer_score < user_score and user_score <= 21:
      dealer_draw()
      dealer_score = sum(dealer_hand)
    
    # Tallying scores
    os.system('clear')
    print(art.logo)
    print(f"Your final hand: {user_hand}; final score: {user_score}")
    print(f"The dealer's final hand: { dealer_hand}; final score: {dealer_score}")
    if user_score > 21:
      print("You went over. You lose 😭")
    elif dealer_score == user_score:
      print("It's a tie and the dealer wins ties. You lose 😭")
    elif user_score < dealer_score and dealer_score <= 21:
      print("The dealer's score is closer to 21. You lose 😭")
    elif user_score <= 21 and user_score > dealer_score:
      print("You're closer to 21 without going over! You win 😁")
    elif user_score <= 21 and dealer_score > 21:
      print("The dealer went over 21! You win 😁")
    blackjack()
        
  else:
    print("Okay, bye!")  

blackjack()