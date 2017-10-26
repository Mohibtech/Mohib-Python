# Example taken from website https://michael0x2a.com/blog/turtle-examples
# Jumping around and changing speed turtle.setposition(x, y) will set the turtle’s position to the coordinates you plug in. 
# (0, 0) is located at the center of the screen – where the turtle first started. 
# Note that you need to make sure the turtle’s pen is up, otherwise it’ll draw a line back to that.

import turtle 

ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()
