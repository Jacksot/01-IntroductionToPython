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

big_boy = rg.SimpleTurtle()
big_boy.pen = rg.Pen('red', 5)
big_boy.speed = 8

size = 50

for k in range(10):
    big_boy.draw_circle(50)

    big_boy.pen_up()
    big_boy.right(30)
    big_boy.forward(20)
    big_boy.left(30)
    big_boy.pen_down()
    size = size - 10

smaller_boy = rg.SimpleTurtle()
smaller_boy.pen = rg.Pen('blue', 1)
smaller_boy.speed = 6

size = 15

for k in range(15):

