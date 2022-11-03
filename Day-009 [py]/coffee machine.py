
## 2/11/2022

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


def enough_resources(drink):
    for item in drink:
        if drink[item] >= resources[item]:
            print(f'You dont have enough {item}')
            return False
    return True
    

def coins():
    print('Please insert coins')
    total = int(input('How many quarters?: '))*0.25
    total += int(input('How many dimes?: '))*0.1
    total += int(input('How many nickels?: '))*0.05
    total += int(input('How many pennies?: '))*0.01
    return total


def transcation(payment, drinkCost):
    if payment >= drinkCost['cost']:
        change = round(payment- drinkCost['cost'],2)
        print(f"Here is ${change} in change")
        global profit
        profit = profit + drinkCost['cost']
        return True
    else:
        print('Sorry that is nnot enought money. Money refunded')
        return False

def makeCoffee(drink, ingredients):
    for item in ingredients:
        resources[item]-= ingredients[item]
    print(f'Here is your {drink}')
        

on = True

print("""
                                       
   _____       __  __            __  __       _             
  / ____|     / _|/ _|          |  \/  |     | |            
 | |     ___ | |_| |_ ___  ___  | \  / | __ _| | _____ _ __ 
 | |    / _ \|  _|  _/ _ \/ _ \ | |\/| |/ _` | |/ / _ \ '__|
 | |___| (_) | | | ||  __/  __/ | |  | | (_| |   <  __/ |   
  \_____\___/|_| |_| \___|\___| |_|  |_|\__,_|_|\_\___|_|     
""")


while on:
    userChoice = input('What would you like? (espresso/latte/cappuccino): ')
    if userChoice == 'off':
        on = False
    elif userChoice == 'report':
        print(f"water :{resources['water']}ml")
        print(f"milk :{resources['milk']}ml")
        print(f"coffee :{resources['coffee']}ml")
        print(f"Money :${profit}")
    else:
        drink = MENU[userChoice]
        if enough_resources(drink['ingredients']):
            payment = coins()
            if transcation(payment, drink):
                makeCoffee(userChoice,drink['ingredients'])
            
            

