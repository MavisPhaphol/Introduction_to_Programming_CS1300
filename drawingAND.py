"""
Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

t.right(90)
t.forward(115) # vertical line
t.left(90)
t.forward(105) # bottom line
t.up()
t.right(180)
t.forward(105) # above bottom line
t.right(90)
t.forward(115) # above vertical line
t.right(90)
t.down()
t.forward(100) # top line

i = 1 # semi-circle
while i < 180:
  t.forward(1)
  t.right(1)
  i = i + 1
  
t.up()
t.right(180)

i = 1 # above semi-circle
while i < 180:
  t.forward(1)
  t.left(1)
  i = i + 1
  
t.right(180)
t.forward(125)
t.right(90)
t.forward(60) # around middle of semi-circle
t.right(90)
t.down() 
t.forward(68) # output
t.up()
t.right(180)
t.forward(68) # above output
t.left(90)
t.forward(60)
t.left(90)
t.forward(125) # back at code line 35
t.left(90)
t.forward(30)
t.right(90)
t.forward(102) # in between vertical line
t.down()
t.forward(75) # first input
t.up()
t.left(90)
t.forward(50)
t.left(90)
t.down()
t.forward(75) # second input
t.up()
t.forward(50) 