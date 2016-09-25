# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 22:22:52 2016

@author: Jacob
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 13:19:21 2016

@author: jds110

--prompt user to go big, or small AND their bet amount
small: choose even or odd. bet+10%
big: choose which numbers. bet*2

-- rolling dice
function for each dice with turtle
random function
random result decides which side of dice

--winning or losing
add winnings to coin amount
don't add anything if user lost

"""
import turtle
import random

wn = turtle.Screen()
wn.bgcolor("lightgreen")
turt = turtle.Turtle()

def square():   
    turt.pendown()
    for i in range(4):
        turt.forward(50)
        turt.left(90)
    turt.penup()

def one():
    
    square()

def two():
    
    turt.goto(-100,100)
    square()
    turt.goto(100, -100)
    square()
    ss
def three():
    
    square()
    turt.goto(-100,100)
    square()
    turt.goto(100, -100)
    square()
    
def four():
    
    turt.goto(-100,100)
    square()
    turt.goto(100, -100)
    square()
    turt.goto(100,100)
    square()
    turt.goto(-100, -100)
    square()
    
def five():
    
    square()    
    turt.goto(-100,100)
    square()
    turt.goto(100, -100)
    square()
    turt.goto(100,100)
    square()
    turt.goto(-100, -100)
    square()
    
    
def six():
    
    turt.goto(-100,100)
    square()
    turt.goto(100, -100)
    square()
    turt.goto(100,100)
    square()
    turt.goto(-100, -100)
    square()
    turt.goto(0,100)
    square()
    turt.goto(0,-100)

currency = int(10)

print("We've given you 10 coins to start, good luck!")

def main(currency):
    bet_type = int(input("Type 1 for small bet, type 2 for big bet: "))
    bet_amount = int(input("How much do you want to bet?: "))
    
    while True:
        if bet_amount > currency:
            print("You don't have enough currency for this bet")
        else:
            if bet_type == 1:
                roll_result = random.randrange(1,2,1)
                users_guess = int(input("Type 1 for odd, type 2 for even: "))
                if roll_result == users_guess:
                    bet_winnings = bet_amount + (bet_amount*.1)
                    print("You won", bet_amount)
                    currency = currency + bet_winnings
                    
                else:
                    print("You lost!")
                    currency = currency - bet_amount
                
            if bet_type == 2:
                roll_result = random.randrange(1,7,1)
                users_guess = int(input("What will the dice land on? 1-6: "))
                
                if roll_result == 1:
                    one()
                elif roll_result == 2:
                    two()
                elif roll_result == 3:
                    three()
                elif roll_result == 4:
                    four()
                elif roll_result == 5:
                    five()
                elif roll_result == 6:
                    six()
                    
                    
                if roll_result == users_guess:
                    bet_winnings = bet_amount + (bet_amount*2)
                    print("The dice was:", roll_result, "You won", bet_amount)
                    currency = currency + bet_winnings
                else:
                    print("The dice was:", roll_result, "You lost!")
                    currency = currency - bet_amount
turtle.bye()
main(currency)