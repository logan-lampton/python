import math

# 3 hot flavors
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Program requirements:

# TODO 1. Print Report
# TODO 2. Check that the resources are sufficient (resources will be reduced each order)
# TODO 3. Ask to insert coins; track the coins entered, change, and give the drink; if not enough, refund the drink and apologize
# TODO 4. Make the coffee and subtract the resources/add the coins to the amount of money (probably need to track each coin)

espresso_cost = MENU["espresso"]["cost"]
latte_cost = MENU["latte"]["cost"]
cappuccino_cost = MENU["cappuccino"]["cost"]

COINS = {"quarters": 0.25, "dimes": 0.1, "nickels": 0.05, "pennies": 0.01}

flavor = input("What would you like?: 'Espresso', 'Latte', or 'Cappuccino': ").lower()

if flavor == "espresso":
    cost = espresso_cost
elif flavor == "latte":
    cost = latte_cost
else:
    cost = cappuccino_cost

print(f"That will cost ${cost}0. Please insert coins.")


def payment():
    """Takes the coins from the user and calculates their value, then gives change"""
    total = cost
    for coin_type in COINS:
        amt_coin_type = float(input(f"How many {coin_type}?: "))
        total = float(total - COINS[coin_type] * amt_coin_type)
        print(f"Thank you, you now owe: ${round(total, 2)}")
    if (total) > 0:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        print(f"Thanks, your change amount is ${round(float(total * -1), 2)}")


payment()

print(f"Here is your {flavor} ☕. Enjoy!")
