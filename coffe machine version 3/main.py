# OOP

class Resources():
    def __init__(self, water, coffe, milk):
        self.water = water
        self.coffe = coffe
        self.milk = milk


    def report(self):
        print(f"You have\n{self.water}ml water\n{self.coffe}mg coffe\n{self.milk}ml milk")


class Coffe():
    def __init__(self, water, coffe, money, milk):
        self.water = water
        self.coffe = coffe
        self.money = money
        self.milk = milk


espresso = Coffe(50, 18, 1.5, 0)
latte = Coffe(200, 24, 2.5, 150)
cappuccino = Coffe(250, 24, 3, 150)
resource = Resources(300, 100, 200)

# OOP
# Function

def make_coffe(resource, coffe_name):
    if resource.water < coffe_name.water or resource.coffe < coffe_name.coffe or resource.milk < coffe_name.milk:
        print("Not enough materials")
    else:
        pay_money = int(input("Please enter money: $"))
        if pay_money < coffe_name.money:
            print("Not enough money")
        elif pay_money > coffe_name.money:
            print(f"Change: {pay_money - coffe_name.money}$")
            resource.water -= coffe_name.water
            resource.coffe -= coffe_name.coffe
            resource.milk -= coffe_name.milk

# Function

flag = True
while flag:
    choice = input("What would you like? (espresso/latte/cappuccino/off/report): ")
    if choice == "off":
        flag = False
    elif choice == "report":
        resource.report()
    elif choice in ["espresso", "latte", "cappuccino"]:
        if choice == "espresso":
            make_coffe(resource, espresso)
        elif choice == "latte":
            make_coffe(resource, latte)
        else:
            make_coffe(resource, cappuccino)
    else:
        print("Please choose one")
