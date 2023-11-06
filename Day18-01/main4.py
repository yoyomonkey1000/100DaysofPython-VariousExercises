import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
gui_screen = turtle.Screen()
colours= ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black"]
angles = [0, 90, 180, 270]
tim.speed(10)
tim.pensize(5)

def random_walker(turtle):
    while True:
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        turtle.setheading(random.choice(angles))
        turtle.forward(10)
        turtle.pencolor((color))



random_walker(tim)

gui_screen.exitonclick()