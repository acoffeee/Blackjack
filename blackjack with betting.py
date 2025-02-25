import random
import math
x = random.randint (1,11)
y = random.randint (1,11)
z = random.randint (1,10)
a = random.randint (1,11)
b = random.randint (1,11)
c = random.randint (1,10)
user_chips = {'chips':1000}
bet = {"bet":0}
choices = {"hit":22, "pass":23}
dealers_cards = [x,y]
users_cards = [a,b]
print (f'dealers cards are: {x} and {y}') 
print (f' you cards are: {a} and {b}')

bet = input(f'your current chip amount is {user_chips["chips"]} \n how much would you like to bet?:')
if int(bet) > user_chips["chips"]:
    bet = input (f'you cant bet chips you dont have, please pick a different ammount:')
user_choice = input ("hit or pass?")
if user_choice in choices:
    if user_choice == "hit":
        print (c)
        if a + b + c > 21:
            print ("busted")
            user_chips ['chips'] -= int(bet)
        else:
            if x + y <= 16:
                print ("dealer hits")
                print (z)
                if x + y + z >21:
                    print ("dealer busted, you win")
                    user_chips ['chips'] += int(bet)
                else:
                    if 21 - (x + y + z) < 21 - (a + b + c):
                        print ("dealer won")
                        user_chips ['chips'] -= int(bet)
                    else:
                        print ("you win")
                        user_chips ['chips'] += int(bet)
            else:
                if 21 - ( a + b + c) < 21 - (x + y):
                    print ("you win")
                    user_chips ['chips'] += int(bet)
                else:
                    print ("dealer wins")
                    user_chips ['chips'] -= int(bet)
    else:
        if x + y <= 16:
                print ("dealer hits")
                print (z)
                if x + y + z >21:
                    print ("dealer busted, you win")
                    user_chips ['chips'] += int(bet)
                else:
                    if 21 - (x + y + c) < 21 - (a + b):
                        print ("dealer won")
                        user_chips ['chips'] -= int(bet)
                    else:
                        print ("you win")
                        user_chips ['chips'] += int(bet)
        else:
                if 21 - ( a + b) < 21 - (x+y):
                    print ("you win")
                    user_chips ['chips'] += int(bet)
                else:
                    print ("dealer wins")
                    user_chips ['chips'] -= int(bet)
else:
    print ("please type valid command")
print (user_chips["chips"])
