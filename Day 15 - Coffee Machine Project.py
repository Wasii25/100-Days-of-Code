MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            'milk': 0,
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

global money
money = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
game_on = True


while game_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ")

    while choice.lower() not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
        print("PLease enter a valid choice")
        choice = input("What would you like? (espresso/latte/cappuccino): ")



    if choice.lower() == 'off':
        game_on = False
        break

    elif choice.lower() == 'report':
        for i in resources:
            print(f"{i}: {resources[i]}")
        print(f'{money}')
        continue

    drink = MENU[choice]

    #CHECK FOR RESOURCES
    def check_resources(order_ingredients):
        for item in order_ingredients:
            if order_ingredients[item] >= resources[item]:
                print(f"Sorry there is not enough {item}")
                return False
            else:
                return True

    def make_coffee():
        for r in resources:
            resources[r] -= MENU[choice]['ingredients'][r]

        print(f"Here is your {choice}☕. Enjoy!")

    def check_transaction():

        pennies = int(input("How many pennies? "))/100
        nickles = int(input("How many nickles? "))/20
        dimes = int(input("How many dimes? "))/10
        quarters = int(input("How many quarters? "))/4

        return pennies + nickles + dimes + quarters


    if check_resources(drink["ingredients"]):
        profit = check_transaction()
        money = money + profit
        if money < MENU[choice]['cost']:
            print("Sorry! That's not enough money. Money refunded.")
            money -= profit
        else:
            if money == MENU[choice]['cost']:
                make_coffee()
            else:
                change = money
                change -= MENU[choice]['cost']
                round(change, 2)
                print(f"Here is your ${change} in change")
                money += MENU[choice]['cost']
                make_coffee()


