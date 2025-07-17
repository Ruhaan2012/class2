"""Outline:
Write a program to set screen size, colour for turtle graphics and draw a polygon using turtle?

Star
Outline:
Write a program to draw a star using a turtle?

Spiral pattern
Outline:
Write a program to draw a square inside a square?

import turtle 
turtle.Screen().bgcolor("orange")
polygon=turtle.Turtle()
sides=6
length=70
angle=360/sides
for i in range(sides):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()

import turtle 
turtle.Screen().bgcolor("blue")
star=turtle.Turtle()
star.right(75)
star.forward(500)
for i in range(4):
    star.right(144)
    star.forward(500)


turtle.done()

import turtle 
turtle.Screen().bgcolor("light blue")
square=turtle.Turtle()
size=0
while True:
    for i in range(4):
        square.forward(size+1)
        square.left(90)
        size=size-5
    size=size+1

        
turtle.done()"""





import turtle 
turtle.Screen().bgcolor("blue")
square=turtle.Turtle()
square.right(75)
square.forward(100)
for i in range(4):
    square.right(144)
    square.forward(100)


turtle.done()