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

input("What would you like?: 'Espresso, Latte, or Cappuccino")