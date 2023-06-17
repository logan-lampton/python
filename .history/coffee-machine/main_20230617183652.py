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

profit = 0

# Program requirements:

# DONE 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)"
# DONE 2.Turn off the Coffee Machine by entering “off” to the prompt.
# DONE 3. Print report
# DONE 4. Check if resources are sufficient
# DONE 5. Process coins
# DONE 6. Check if the transaction is successful
# DONE 7. Make coffee


# def calculate_cost(flavor):
#     if flavor == "espresso":
#         return MENU["espresso"]["cost"]
#     if flavor == "latte":
#         return MENU["latte"]["cost"]
#     else:
#         return MENU["cappuccino"]["cost"]


is_on = True
while is_on:
    flavor = input(
        "What would you like?: 'Espresso', 'Latte', or 'Cappuccino': "
    ).lower()
    if flavor == "off":
        print("Shutting down coffee machine. Goodbye.")
        is_on = False
    elif flavor == "report":
        print(f"Current resources are: {resources}")
        print(f"Current profit is: ${profit}0")
    else:
        drink = MENU[flavor]
        remaining_water = resources["water"] - drink["ingredients"]["water"]
        remaining_coffee = resources["coffee"] - drink["ingredients"]["coffee"]
        if "milk" in drink["ingredients"]:
            remaining_milk = resources["milk"] - drink["ingredients"]["milk"]
            if remaining_milk < 0:
                print("Sorry there is not enough milk")
        elif remaining_water < 0:
            print("Sorry there is not enough water")
        elif remaining_coffee < 0:
            print("Sorry there is not enough coffee")
        else:
            resources["water"] = remaining_water
            resources["coffee"] = remaining_coffee
            resources["milk"] = remaining_milk
            cost = drink["cost"]
            print(f"That will cost ${cost}0. Please insert coins.")
            total = cost
            for coin_type in COINS:
                amt_coin_type = float(input(f"How many {coin_type}?: "))
                total = float(total - COINS[coin_type] * amt_coin_type)
                print(f"Thank you, you now owe: ${round(total, 2)}")
            if (total) > 0:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                profit += cost
                print(f"Thanks, your change amount is ${round(float(total * -1), 2)}")
                print(f"Here is your {flavor} ☕. Enjoy!")
