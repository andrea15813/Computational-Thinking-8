import turtle, time, random
from utils import *
import random

time.sleep (2)
print ("dog race")
# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-200
y1 =200
x2 =-200
y2 =87
x3 =-200
y3 =-87
x4 =-200
y4 =-200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("park")
t1 = create_sprite("dog",x1,y1)
t2 = create_sprite("fox",x2,y2)
t3 = create_sprite("corgi",x3,y3)
t4 = create_sprite("flower",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # Sprite 1 and 4 are the only ones that can win. 4 is a random number so it could be faster or slower.
for i in range(45):
     x1+=10
     x2+=5
     x3+=3
     x4+=random.randint(5,20)
     time.sleep (0.1)

     t1.goto(x1,y1)
     t2.goto(x2,y2)
     t3.goto(x3,y3)
     t4.goto(x4,y4)

     window.update()
     time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
# # Whatever player got the farthest would win and a message would be displayed in the terminal
if x1 >= x2 and x1 >= x3 and x1 >= x4:
     print("player 1 wins!")
elif x2>=x1 and x2>=x3 and x2>=x4:
     print("player 2 wins!")
elif x3>=x1 and x3>=x2 and x3>=x4:
     print("player 3 wins!")
elif x4>=x1 and x4>=x2 and x4>=x3:
     print("player 4 wins!")


turtle.exitonclick()