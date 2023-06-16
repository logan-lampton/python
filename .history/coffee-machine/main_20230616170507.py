import math
import os

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

COINS = {"quarters": 0.25, "dimes": 0.1, "nickels": 0.05, "pennies": 0.01}


# Program requirements:

# DONE 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)"
# DONE 2.Turn off the Coffee Machine by entering “off” to the prompt.
# DONE 3. Print report
# TODO 4. Check if resources are sufficient
# DONE 5. Process coins
# DONE 6. Check if the transaction is successful
# DONE 7. Make coffee


def calculate_cost(flavor):
    if flavor == "espresso":
        return MENU["espresso"]["cost"]
    if flavor == "latte":
        return MENU["latte"]["cost"]
    else:
        return MENU["cappuccino"]["cost"]


def calculate_resource_cost(flavor):
    if MENU[flavor]["ingredients"] == "espresso":
        resources["water"] = resources["water"] - MENU[flavor]["ingredients"]["water"]
        resources["coffee"] = (
            resources["coffee"] - MENU[flavor]["ingredients"]["coffee"]
        )
        return
    else:
        resources["water"] = resources["water"] - MENU[flavor]["ingredients"]["water"]
        resources["coffee"] = (
            resources["coffee"] - MENU[flavor]["ingredients"]["coffee"]
        )
        resources["milk"] = resources["milk"] - MENU[flavor]["ingredients"]["milk"]
    # return

    print(resources["water"], resources["milk"], resources["coffee"])


def coffee_machine():
    """Creates a flavor of coffee based on user input / tracks the resources available"""
    power = True
    while power:
        flavor = input(
            "What would you like?: 'Espresso', 'Latte', or 'Cappuccino': "
        ).lower()

        if flavor == "off":
            print("Shutting down coffee machine. Goodbye.")
            break
        elif flavor == "report":
            print(f"Current resources are: {resources}")
            flavor = input(
                "What would you like?: 'Espresso', 'Latte', or 'Cappuccino': "
            ).lower()
        else:
            cost = calculate_cost(flavor)

        calculate_resource_cost(flavor)

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


coffee_machine()
