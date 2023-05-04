import turtle
wn = turtle.Screen()
wn.setup(width=400, height=400)
red = turtle.Turtle() # Assigning "Red" as name of the turtle

red.fillcolor("yellow")
red.begin_fill()
red.circle(200)
red.end_fill()
red.penup()
red.goto(-120,300)
red.pendown()
red.pencolor("black")
red.pensize(5)
red.lt(25)
for i in range(1,50):
 red.rt(1)
 red.fd(1)
red.penup()
red.goto(100,300)
red.pendown()
red.lt(50)
for i in range(1,50):
 red.rt(1)
 red.fd(1)
red.penup()
red.goto(-25,70)
red.pendown()
for i in range(1,50):
    red.lt(1)
    red.fd(1)
red.penup()
red.goto(-22,70)
red.pendown()
red.pensize(1)
red.pencolor("red")


def curve(): # Method to draw curve
    for i in range(200): # To draw the curve step by step
        red.right(1)
        red.forward(1)

def heart():  # Method to draw full Heart
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curve() # Left Curve
    red.left(120)
    curve() # Right Curve
    red.forward(112)
    red.end_fill()

heart()

turtle.done()