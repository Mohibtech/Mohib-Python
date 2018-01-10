# Draw a Koch snowflake
import turtle

def koch(t,size, order):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            #t.forward(a/3)
            koch(t, size/3, order-1)
            t.left(angle)
    
wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")

t = turtle.Turtle() 
t.color("blue") 
t.pensize(3)

# Test
koch(t,500, 3)

wn.mainloop()
