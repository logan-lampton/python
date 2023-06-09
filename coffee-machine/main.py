# Program requirements:

# DONE 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)"
# DONE 2.Turn off the Coffee Machine by entering “off” to the prompt.
# DONE 3. Print report
# DONE 4. Check if resources are sufficient
# DONE 5. Process coins
# DONE 6. Check if the transaction is successful
# DONE 7. Make coffee

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


def is_resource_available(flavor_ingredients):
    """Checks if the ingredients are available for a selected flavor"""
    for item in flavor_ingredients:
        if flavor_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def make_coffee(flavor_name, flavor_ingredients):
    """Deduct the ingredients required to make the given coffee from the total resources"""
    for item in flavor_ingredients:
        resources[item] -= flavor_ingredients[item]
    print(f"Here is your {flavor_name} ☕. Enjoy!")


def process_coins(cost):
    """Prompts the user to pay coins for the given cost and returns their change if enough coins are provided"""
    print(f"That will cost ${cost}0. Please insert coins.")
    total = cost
    for coin_type in COINS:
        amt_coin_type = float(input(f"How many {coin_type}?: "))
        total = float(total - COINS[coin_type] * amt_coin_type)
        print(f"Thank you, you now owe: ${round(total, 2)}")
    if (total) > 0:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        print(f"Thanks, your change amount is ${round(float(total * -1), 2)}")
        return True


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
        if is_resource_available(drink["ingredients"]):
            cost = drink["cost"]
            if process_coins(cost):
                profit += cost
                make_coffee(flavor, drink["ingredients"])
