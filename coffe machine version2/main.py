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
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins (in dollars):")
    total = float(input("Amount: "))
    return total

def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 1)
        print(f"Change: ${change}")
        profit += drink_cost
        return True
    else:
        print("Not enough money. Refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your {drink_name}!")

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/off/report): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Resources: Water - {resources["water"]}ml, Milk - {resources["water"]}ml, Coffee - {resources["water"]}g")
        print(f"Profit: ${profit}")
    elif choice in ["espresso", "latte", "cappuccino"]:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


