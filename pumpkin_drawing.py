# Pumpkin Drawing
# Author: illia Nyshpor
# Date: 31.10.23

import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

pumpkin.penup()
pumpkin.color("green")
pumpkin.pensize(50)
pumpkin.setposition(0,110)

pumpkin.pendown()
pumpkin.forward(20)
pumpkin.right(90)
pumpkin.forward(10)
pumpkin.right(90)
pumpkin.forward(20)

pumpkin.penup()

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-200, -100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# Nose
carver.penup()
carver.setposition(0, 0)
carver.begin_fill()
carver.forward(10)
carver.left(120)
carver.forward(10)
carver.left(120)
carver.forward(10)
carver.end_fill()
carver.penup()

#eye
carver.penup()
eye = carver.clone()
eye.color("red")

carver.setposition(-50, 20)
carver.pendown()
carver.begin_fill()
carver.backward(30)
carver.right(120)
carver.backward(30)
carver.right(120)
carver.backward(30)
carver.end_fill()

eye.setposition(-50, 20)
eye.hideturtle()
eye.pendown()
eye.begin_fill()
eye.backward(20)
eye.right(120)
eye.backward(20)
eye.right(120)
eye.backward(20)
eye.end_fill()

carver.penup()
eye.penup()

#eye 2
carver.penup()
carver.setposition(40, 20)
carver.pendown()
carver.begin_fill()
carver.forward(30)
carver.left(120)
carver.forward(30)
carver.left(120)
carver.forward(30)
carver.end_fill()

eye.setposition(40, 20)
eye.hideturtle()
eye.pendown()
eye.begin_fill()
eye.forward(20)
eye.left(120)
eye.forward(20)
eye.left(120)
eye.forward(20)
eye.end_fill()

eye.penup()
carver.penup()

# mouth
carver.setposition(0, -50)
carver.pensize(10)
carver.pendown()
carver.right(60)
carver.forward(30)

turtle.done()