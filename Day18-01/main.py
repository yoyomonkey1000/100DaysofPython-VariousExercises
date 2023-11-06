
# PLaying with the turtle graphics
# Created some functions which are shapes
# random shape drawer

from turtle import Turtle, Screen
import random


def draw_triangle(turtle):
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)


def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)


def draw_circle(turtle):
    for _ in range(360):
        turtle.forward(1)
        turtle.left(1)


timmy_the_turtle = Turtle()

for x in range(5):
    timmy_the_turtle.forward(random.randint(1, 10))
    shape = random.randint(1, 3)
    if shape == 1:
        draw_circle(timmy_the_turtle)
    elif shape == 2:
        draw_triangle(timmy_the_turtle)
    else:
        draw_square(timmy_the_turtle)
    timmy_the_turtle.left(random.randint(1, 180))



playground = Screen()

playground.exitonclick()
