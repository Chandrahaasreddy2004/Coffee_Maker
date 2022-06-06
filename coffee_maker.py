logo='''

    __   ___   _____  _____  ___    ___      ___ ___   ____  __  _    ___  ____  
   /  ] /   \ |     ||     |/  _]  /  _]    |   |   | /    ||  |/ ]  /  _]|    \ 
  /  / |     ||   __|| 
    __/  [_  /  [_     | _   _ ||  o  ||  ' /  /  [_ |  D  )
 /  /  |  O  ||  |_  |  |_|    _]|    _]    |  \_/  ||     ||    \ |    _]|    / 
/   \_ |     ||   _] |   _]   [_ |   [_     |   |   ||  _  ||     \|   [_ |    \ 
\     ||     ||  |   |  | |     ||     |    |   |   ||  |  ||  .  ||     ||  .  \
 \____| \___/ |__|   |__| |_____||_____|    |___|___||__|__||__|\_||_____||__|\_|
                                                                                 
'''
print(logo)


def sufficent(choice, number):
    for item in choice:
        if(choice[item]*number>resources[item]):
            print(f"There is no sufficent {item} to make {coffee}")
            break
        else:
            resources[item]=resources[item]-choice[item]
            return True


menu = {
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


latte=24
espresso=1.5
cappuccino=3


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def total_money():
    quaters=int(input("quaters"))
    dimes=int(input("dimes"))
    nickles=int(input("nickles"))
    pennis=int(input("penis"))
    return  round((quaters*0.25+dimes*0.10+nickles*0.05+pennis*-0.01),2)


a=  False
while a is not True:
    coffee=input("What would you like to have.espresso/latte/cappuccino")
    if (coffee == "latte"):
        number = int(input(f"Enter how many {coffee} do you want"))
        choice = menu[coffee]["ingredients"]
        decision = sufficent(choice, number)
        if (decision == True):
            money = total_money()
            if(money>=(2.5*number)):
                give_money =round(money-(number*2.5),2)
                profit=profit+(2.5*number)
                print(f"Enjoy your {coffee}.Tke your remaining {give_money}")
            else:
                print(f"The money you gave is not sufficent to get {coffee}")



    elif (coffee=="espresso"):
        number = int(input(f"Enter how many {coffee} do you want"))
        choice = menu[coffee]["ingredients"]
        decision = sufficent(choice, number, coffee)
        if (decision == True):
            money = total_money()
            if(money>=1.5*number):
                give_money = round(money - (number * 0.25),2)
                profit=profit+(number*1.5)
                print(f"Enjoy your {coffee}.Take your remaining money{give_money}")
            else:
                print(f"The money you gave is not suficet to get {coffee}")


    elif(coffee=="cappuccino"):
        number = int(input(f"Enter how many {coffee} do you want"))
        choice = menu[coffee]["ingredients"]
        decision = sufficent(choice, number, coffee)
        if (decision == True):
            money = total_money()
            if(money>3*number):
                give_money = round(money - (number * 0.25),2)
                profit=profit+(number*3)
                print(f"Enjoy your {coffee}.Take your remaining money{give_money}")
            else:
                print(f"The money you gave is not sufficent to get {coffee}")


    elif coffee=="off":
        print(f"profit={profit}")
        a=True


    elif(coffee=="report"):
        print(resources)


    else:
        print(f"Sry {coffee} is not avaliable")




