from art import logo, vs
from game_data import data
import random
import os


def display_celebrity(celebrity, position):
    """Takes a celebrity and a position and prints a compare statement of the celebrity info"""
    compare = position
    name = celebrity["name"]
    description = celebrity["description"].lower()
    country = celebrity["country"]
    if (
        description[0] == "a"
        or description[0] == "e"
        or description[0] == "i"
        or description[0] == "o"
        or description[0] == "u"
    ):
        print(f"Compare {compare}: {name}, an {description} from {country}")
    else:
        print(f"Compare {compare}: {name}, a {description} from {country}")

number_correct = 0
celebrity1 = random.choice(data)
celebrity2 = random.choice(data)
while celebrity2 == celebrity1:
    celebrity2 = random.choice(data)


def high_low():
    global celebrity1
    global celebrity2
    global number_correct
    playing = True
    while playing:
        print(logo)
        print(f"Number correct: {number_correct}")
        display_celebrity(celebrity1, "A")
        print(vs)
        display_celebrity(celebrity2, "B")
        selection = input("Who has more followers? Type 'A' or 'B': ").lower()
        follower_count1 = celebrity1["follower_count"]
        follower_count2 = celebrity2["follower_count"]
        if follower_count1 > follower_count2:
            loser = celebrity2
            winner = celebrity1
        else:
            loser = celebrity1
            winner = celebrity2
        if (selection == "a" and winner == celebrity1) or (
            selection == "b" and winner == celebrity2
        ):
            print(
                f"Correct! 😁 {winner['name']} has {winner['follower_count']}M followers, which is more than {loser['name']}'s {loser['follower_count']}M followers"
            )
            whether_continue = input(
                "Continue to the next question? Type 'Y' or 'N': "
            ).lower()
            if whether_continue == "y":
                celebrity1 = winner
                celebrity2 = random.choice(data)
                while celebrity2 == celebrity1 or celebrity2 == loser:
                    celebrity2 = random.choice(data)
                number_correct += 1
                os.system("clear")
            else:
                playing = False
                print(f"Number correct: {number_correct}")
        else:
            playing = False
            print(
                f"Sorry! 😟 {loser['name']} has {loser['follower_count']}M followers, which is less than {winner['name']}'s {winner['follower_count']}M followers. You lose."
            )
            print(f"Number correct: {number_correct}")


high_low()
