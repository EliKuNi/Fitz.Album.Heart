

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
    t.up()
    t.right(-96)
    t.down()
    t.forward(15)
    t.up()
    t.right(-83)
    t.down()
    t.forward(25)
    t.right(90)
    t.forward(15)
    t.right(93)
    t.forward(20)
    

#screen.bgpic()
body()
t.screen.exitonclick()
