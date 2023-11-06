from turtle import Turtle, Screen
import random

colours= ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black"]
timo= Turtle()
def drawshape(turtle, sides):
    angle = 360 / sides
    for x in range(sides):
        turtle.right(angle)
        turtle.forward(100)

for shape_side in range(3,16):
    timo.color(random.choice(colours))
    drawshape(timo,shape_side)


turtle_screen = Screen()
turtle_screen.exitonclick()