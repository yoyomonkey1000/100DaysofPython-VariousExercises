import turtle

#create a turtle object from the turtle class

timmy = turtle.Turtle()
print(timmy)
jimmy = turtle.Turtle()


my_screen = turtle.Screen()
timmy.shape("turtle")
timmy.color("coral")

for  _ in range (1, 9):
    for _ in range(1,5):
        jimmy.left(10)
        jimmy.forward(100)
        jimmy.left(90)
        timmy.forward(100)
        timmy.left(90)
    timmy.left(45)
    jimmy.left(45)

print(my_screen.canvheight, "height")
print(my_screen.canvwidth, "width")
my_screen.exitonclick()
