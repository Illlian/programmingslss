# Functions with turtle
# Illia Nyshpor
# Date: 28.11.23

import turtle

lewis = turtle.Turtle()

lewis.color("green")
lewis.shape("turtle")
lewis.speed(0)

def squared(num: float) -> float:
    return num ** 2

def draw_square(length: float) -> None:
    for _ in range(4):
        lewis.forward(length)
        lewis.left(90)

for i in range(20):
    draw_square(squared(i))

turtle.done()