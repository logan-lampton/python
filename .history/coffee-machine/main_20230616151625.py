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

cost = input("What would you like?: 'Espresso', 'Latte', or 'Cappuccino': ").lower()
if cost == "espresso":
    cost = espresso_cost
elif cost == "latte":
    cost = latte_cost
else:
    cost = cappuccino_cost

print(f"That will cost ${cost}0. Please insert coins.")

amt_quarters = float(input("How many quarters?: "))
amt_dimes = float(input("How many dimes?: "))
amt_nickels = float(input("How many nickels?: "))
amt_pennies = float(input("How many pennies?: "))


def money_total(amt_quarters, amt_dimes, amt_nickels, amt_pennies):
    """Takes the coins from the user and calculates their value"""
    coin_sum = (
        amt_quarters * 0.25 + amt_dimes * 0.1 + amt_nickels * 0.05 + amt_pennies * 0.01
    )
    change = coin_sum - cost
    if (coin_sum - cost) < 0:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Thanks, your change amount is ${change}")


money_total(amt_quarters, amt_dimes, amt_nickels, amt_pennies)
