import turtle
turtle.bgcolor()

square=turtle.Turtle()
square.speed(20)
square.pencolor("red")
for i in range(400):
    square.forward(i)
    square.left(91)