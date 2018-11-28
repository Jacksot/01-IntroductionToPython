"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Tyrique Jackson.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

red_boy = rg.SimpleTurtle()
red_boy.pen = rg.Pen('red', 5)
red_boy.speed = 10

size = 50

for k in range(4):
    red_boy.draw_circle(50)

    red_boy.pen_up()
    red_boy.left(90)
    red_boy.forward(90)
    red_boy.right(90)
    red_boy.forward(1)
    red_boy.pen_down()
    size = size - 10

blue_boy = rg.SimpleTurtle()
blue_boy.pen = rg.Pen('blue', 5)
blue_boy.speed = 10

size = 50

for k in range(4):

    blue_boy.draw_circle(50)

    blue_boy.pen_up()
    blue_boy.right(30)
    blue_boy.forward(90)
    blue_boy.left(30)
    blue_boy.forward(1)
    blue_boy.pen_down()
    size = size - 10

yellow_boy = rg.SimpleTurtle()
yellow_boy.pen = rg.Pen('yellow', 5)
yellow_boy.speed = 10

size = 50

for k in range(4):

    yellow_boy.draw_circle(50)

    yellow_boy.pen_up()
    yellow_boy.right(150)
    yellow_boy.forward(90)
    yellow_boy.left(150)
    yellow_boy.forward(1)
    yellow_boy.pen_down()
    size = size - 10

green_boy = rg.SimpleTurtle()
green_boy.pen = rg.Pen('green', 5)
green_boy.speed = 10

size = 50

for k in range(4):
    green_boy.draw_circle(50)

    green_boy.pen_up()
    green_boy.left(270)
    green_boy.forward(90)
    green_boy.right(270)
    green_boy.forward(1)
    green_boy.pen_down()
    size = size - 10

orange_boy = rg.SimpleTurtle()
orange_boy.pen = rg.Pen('orange', 5)
orange_boy.speed = 10

size = 50

for k in range(4):

    orange_boy.draw_circle(50)

    orange_boy.pen_up()
    orange_boy.right(210)
    orange_boy.forward(90)
    orange_boy.left(210)
    orange_boy.forward(1)
    orange_boy.pen_down()
    size = size - 10

purple_boy = rg.SimpleTurtle()
purple_boy.pen = rg.Pen('purple', 5)
purple_boy.speed = 10

size = 50

for k in range(4):

    purple_boy.draw_circle(50)

    purple_boy.pen_up()
    purple_boy.right(330)
    purple_boy.forward(90)
    purple_boy.left(330)
    purple_boy.forward(1)
    purple_boy.pen_down()
    size = size - 10

gray_boy = rg.SimpleTurtle()
gray_boy.pen = rg.Pen('gray', 5)
gray_boy.speed = 10

size = 50

for k in range(1):

    gray_boy.draw_circle(50)

window.close_on_mouse_click()