import turtle, time, random
from utils import *
#my game makes pineapples when you press p and when you get enough pineapples you can buy a turtle
#the goal is to make as many pineapples as you can
# Section 1 - setup
set_background("pond")

# TODO - create at least two variables and set their starting value. ex: cookies = 0
pineapples=0
money=0
turtles=0



# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -200,150)
message_sprite.hideturtle()




#when you press the p key it gives you a pineapple and $2. It also spawns a pineapple sprite

def add_pineapple ():
   global pineapples, money
   pineapples+=1
   money+=2

   x=random.randint(-200,200)
   y=random.randint(-200,200)
   t1=create_sprite("pineapple",x,y)
window.onkeypress(add_pineapple, "p")

#the t key buys a turtle if you have more than $150
def buy_turtle ():
    global money,turtles
    if money>=150:
        turtles+=1
        money-=150

        x=random.randint(-200,200)
        y=-200
        t2=create_sprite("turtle",x,y)
window.onkeypress(buy_turtle,"t")

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control





# over time, if you buy a turtle it will automatically give you that many pineapples and money.
window.listen()
for i in range(1000000000):
    pineapples+=turtles
    money+=turtles
    time.sleep(0.5)

    # OPTIONAL - use the message sprite to say a message
    message_sprite.clear()
    message_sprite.write(f"pineapples-{pineapples}\nmoney-{money}\nturtles-{turtles}",font=("arial",30,"normal"))

    time.sleep(0.01)
    window.update()