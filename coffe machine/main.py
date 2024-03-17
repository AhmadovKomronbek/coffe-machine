import ascii
import data
import color
# We have items
water = data.resources["water"]
milk = data.resources["milk"]
coffee = data.resources["coffee"]

# profit
profit = data.profit

# menu
menu = data.MENU

# function
def not_enough(item):
    print(f"{color.RED}Sorry, not enough {item}.{color.END}\n")
# espresso
def espresso():
    global profit
    global water
    global coffee
    global amount

    profit = amount - menu["espresso"]["cost"]
    water -= menu["espresso"]["ingredients"]["water"]
    coffee -= menu["espresso"]["ingredients"]["coffee"]
# latte
def latte():
    global amount
    global profit
    global milk
    global water
    global coffee

    profit = amount - menu["latte"]["cost"]
    water -= menu["latte"]["ingredients"]["water"]
    coffee -= menu["latte"]["ingredients"]["coffee"]
    milk -= menu["latte"]["ingredients"]["milk"]

# cappuccino
def cappuccino():
    global profit
    global milk
    global water
    global coffee
    global amount

    profit = amount - menu["cappuccino"]["cost"]
    water -= menu["cappuccino"]["ingredients"]["water"]
    coffee -= menu["cappuccino"]["ingredients"]["coffee"]
    milk -= menu["cappuccino"]["ingredients"]["milk"]
# Flag
flag = True
print(f"{color.BROWN}{ascii.logo}{color.END}")

while flag:
    print(f"{color.CYAN}Name             Cost\n"
          "espresso         1.5$\n"
          "latte            2.5$\n"
          f"cappuccino       3$\n{color.END}")
    chose_coffe = input("What would you like? (espresso/latte/cappuccino/off): ").lower()
    if chose_coffe == "espresso" or chose_coffe == "latte" or chose_coffe == "cappuccino" or chose_coffe == "off":
        if chose_coffe == "espresso":
            if water < 50 or coffee < 18:
                if water < 50:
                    not_enough("water")
                else:
                    not_enough("coffee")
            else:
                print("Please insert coins (in dollars)")
                amount = float(input("Amount: ").lower())
                print(amount)
                if amount < 1.5:
                    print(f"{color.RED}Not enough coin{color.END}\n")
                else:
                    espresso()
                    print(f"Change: ${profit}")
                    print(f"{color.GREEN}Enjoy your espresso!{color.END}\n")

        elif chose_coffe == "latte":
            if water < 200 or milk < 150 or coffee < 24:
                if water < 200:
                    not_enough("water")
                elif milk < 150:
                    not_enough("milk")
                else:
                    not_enough("coffee")
            else:
                print("Please insert coins (in dollars)")
                amount = float(input("Amount: ").lower())
                if amount < 2.5:
                    print(f"{color.RED}Not enough coin{color.END}\n")
                else:
                    latte()
                    print(f"Change: ${profit}")
                    print(f"{color.GREEN}Enjoy your latte!{color.END}\n")

        elif chose_coffe == "cappuccino":
            if water < 250 or milk < 100 or coffee < 24:
                if water < 250:
                    not_enough("water")
                elif milk < 100:
                    not_enough("milk")
                else:
                    not_enough("coffee")
            else:
                print("Please insert coins (in dollars)")
                amount = float(input("Amount: ").lower())
                if amount < 3:
                    print(f"{color.RED}Not enough coin{color.END}\n")
                else:
                    cappuccino()
                    print(f"Change: ${profit}")
                    print(f"{color.GREEN}Enjoy your cappuccino!{color.END}\n")
        else:
            print(f"{color.YELLOW}Off{color.END}")
            flag = False
    else:
        print("Please choose one !!!")
