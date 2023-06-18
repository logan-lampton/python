from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
process_coins = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    order = input(
            "What would you like?: 'Espresso', 'Latte', or 'Cappuccino': "
        ).lower()
    if order == "off":
        print("Shutting down coffee machine. Goodbye.")
        is_on = False
    elif order == "report":
        # 1. Print report
        coffee_maker.report()
        process_coins.report()
    else:
        menu_item = menu.find_drink(order)
        # 2. Check if resources are sufficient
        if coffee_maker.is_resource_sufficient(menu_item):
            # 3. Process coins
            cost = menu_item.cost
            payment = process_coins.make_payment(cost)
            # 4. Check if transaction was successful
            if payment:
                coffee_maker.make_coffee(menu_item)