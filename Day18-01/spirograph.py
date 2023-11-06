import turtle
import random

turtle.colormode(255)
angle= random.randint(1,360)

def draw_circle(turtle):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.pencolor(color)
    turtle.circle(100)

tim = turtle.Turtle()
tim.speed("fastest")
print(angle)
for x in range(int(360/angle)):
    print(x)
    draw_circle(tim)
    tim.setheading(360/angle)


spiro_screen = turtle.Screen()
spiro_screen.exitonclick()

