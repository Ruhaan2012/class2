import turtle 
turtle.Screen().bgcolor("orange")
square=turtle.Turtle()
sides=4
length=100
angle=360/sides
for i in range(sides):
    square.forward(length)
    square.right(angle)
turtle.done()
