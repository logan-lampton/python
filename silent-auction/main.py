import os

# logo
from art import logo
print(logo)
print("Welcome to Silent Auction. You can silently bid against others and we will provide the winner of the auction to you.")

bidding_finished = False
bidding_dictionary = {}

def calculate_highest_bid():
  largest_value = 0
  for person in bidding_dictionary:
    bid = bidding_dictionary[person]
    if bid > largest_value:
      largest_value = bidding_dictionary[person]
      winner = person
  print(f"{winner} wins with a bid of ${largest_value}")
  
# Possibly repeat
# 1. ask for name input
while not bidding_finished:
  name = input("What is your name?:\n")
# 2. ask for bid price input
  bid_amount = int(input("What amount would you like to bid?: Provide amount in $ (don't add $):\n"))
# 3. Add name and bid into a dictionary as a key and value
  bidding_dictionary[name] = bid_amount
  print(bidding_dictionary)
# 4. Ask if there are any other users who want to bid
  # if yes: clear the screan and repeat
  #  if no: find the highest bid in the dictionary and declare them as the winner
  additional_bidder = input("Is there anyone else that would like to bid? Type: yes or no\n").lower()
  if additional_bidder == "no":
    bidding_finished = True
    calculate_highest_bid()
  else:
    os.system('clear')
