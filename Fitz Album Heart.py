

import turtle

#screen = turtle.Screen()
#screen.bgpic('C:\Users\Alfonso\Pictures\CODESSS\forest.jpg')

BODY_COLOR = 'magenta'

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Fitz Album Heart")
turtle.bgcolor("#17232f")

def body():
    """ draws the body """
    t.pensize(3)
    t.pencolor("magenta")
    #t.speed(15)

    # drawing the heart symbol
    t.up()
    t.right(100)
    t.forward(155)
    t.right(70)
    t.forward(10)
    t.left(170)
    t.down()
    t.forward(18)
    t.right(-96)
    t.down()
    t.forward(15)
    t.right(-83)
    t.down()
    t.forward(25)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(37)
    t.left(90)
    t.forward(18)
    t.left(89.99)
    t.forward(60)
    t.right(85)
    t.forward(15)
    t.right(95)
    t.forward(93)
    t.right(-90)
    t.forward(17)
    t.right(-90)
    t.forward(120)


#screen.bgpic()
body()
t.screen.exitonclick()
