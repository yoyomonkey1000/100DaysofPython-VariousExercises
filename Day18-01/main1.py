from turtle import Turtle, Screen


def dashed_line(turtle, length = 150):
    for _ in range(length//10):
        turtle.forward(length/20)
        turtle.penup()
        turtle.forward(length / 20)
        turtle.pendown()


tim_the_turtle = Turtle()
dashed_line(tim_the_turtle)

test = Screen()
test.exitonclick()
