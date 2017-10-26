# https://www.blog.pythonlibrary.org/2012/08/06/python-using-turtles-for-drawing/

import turtle
 
myTurtle = turtle.Turtle(shape="turtle")
myTurtle.circle(50)
 
myTurtle.penup()
myTurtle.setposition(-120, 0)
myTurtle.pendown()
myTurtle.circle(50)
 
myTurtle.penup()
myTurtle.setposition(60,60)
myTurtle.pendown()
myTurtle.circle(50)
 
myTurtle.penup()
myTurtle.setposition(-60, 60)
myTurtle.pendown()
myTurtle.circle(50)
 
myTurtle.penup()
myTurtle.setposition(-180, 60)
myTurtle.pendown()
myTurtle.circle(50)
 
turtle.getscreen()._root.mainloop()
