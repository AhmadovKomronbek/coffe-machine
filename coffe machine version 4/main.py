# Todo import other files
import color
import logo

# Todo Class

# Resource
class ResourceClass():
    def __init__(self, water, coffe, milk):
        self.water = water
        self.coffe = coffe
        self.milk = milk

    def report(self):
        print(f"{color.CYAN}You have\n{self.water}ml water\n{self.coffe}mg coffe\n{self.milk}ml milk\n{color.END}")

# Coffe
class Coffe():
    def __init__(self, water, coffe, cost, name):
        self.milk_bool = False
        self.milk = 0
        self.water = water
        self.coffe = coffe
        self.cost = cost
        self.name = name

    def add_milk(self, milk):
        self.milk = milk
        self.milk_bool = True


# Todo Resource
resource = ResourceClass(300, 100, 200)

# Todo Coffe
# espresso
espresso = Coffe(50, 18, 1.5, "espresso")

# latte
latte = Coffe(200, 24, 2.5, "latte")
latte.add_milk(150)

# cappuccino
cappuccino = Coffe(250, 24, 3, "cappuccino")
cappuccino.add_milk(100)

# Todo Class
# Todo Function

# Check coins function
def check_coins(user_coins, coffe_cost):
    if user_coins < coffe_cost:
        print(f"{color.RED}Not enough coins\n{color.END}")
        return False

    elif user_coins >= coffe_cost:
        return True


# Check resources function
def check_resources(resources, coffe_name):
    if resources.water < coffe_name.water:
        print(f"{color.RED}Not enough water !!!\n{color.END}")
        return False

    elif resources.coffe < coffe_name.coffe:
        print(f"{color.RED}Not enough coffe !!!\n{color.END}")
        return False

    elif resources.milk < coffe_name.milk:
        print(f"{color.RED}Not enough milk !!!\n{color.END}")
        return False

    else:
        return True

def coffe_maker(resources, coffe_name):
    if check_resources(resources, coffe_name):
        print(f"{color.GREEN}Please insert coins (in dollars)\n{color.END}")
        user_coins = float(input(f"{color.GREEN}Amount: {color.END}"))
        if check_coins(user_coins, coffe_name.cost):
            print(f"{color.CYAN}Change: ${user_coins - coffe_name.cost}\n{color.END}")
            print(f"{color.CYAN}Enjoy your {coffe_name.name}!\n{color.END}")

            resources.water -= coffe_name.water
            resources.coffe -= coffe_name.coffe

            if coffe_name.milk_bool:
                resource.milk -= coffe_name.milk

# Todo Function
# Todo Main code

# while loop
print(f"{color.YELLOW}{logo.logo}{color.END}")

flag = True
while flag:
    user_choose = input(f"{color.GREEN}What would you like? (espresso/latte/cappuccino/report/off): {color.END}").lower()
    if user_choose == "off":
        flag = False

    elif user_choose == "report":
        resource.report()

    elif user_choose == "espresso":
        coffe_maker(resource, espresso)

    elif user_choose == "latte":
        coffe_maker(resource, latte)

    elif user_choose == "cappuccino":
        coffe_maker(resource, cappuccino)

    else:
        print(f"{color.YELLOW}Please choose one !!!\n{color.END}")

# Todo Main code
