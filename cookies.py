# Cookies
# Illia Nyshpor
# 21.11.23 / 23.11.23

import turtle
import random

h = turtle.window_height() // 2
w = turtle.window_width() // 2


baker_turtle = turtle.Turtle()
baker_turtle.speed(0)

def make_cookie(x: int, y: int):
    """Draws a cookie on the screeen at (x y)
    Params:
    x - the x-coordinate of the center cookie
    y - the y-coordinate of the center cookie
    """
    
    baker_turtle.color("brown")

    # Draw outline of cookie
    baker_turtle.penup()
    baker_turtle.goto(-5 + x, -30 + y)
    baker_turtle.pendown()
    baker_turtle.begin_fill()
    baker_turtle.circle(30)
    baker_turtle.end_fill()
    baker_turtle.penup()

    # Add chips
    baker_turtle.color("black")

    baker_turtle.goto(0 + x, 0+ y)
    baker_turtle.stamp()

    baker_turtle.goto(10 + x, 10 + y)
    baker_turtle.stamp()

    baker_turtle.goto(-10 + x, -10 + y)
    baker_turtle.stamp()

    baker_turtle.goto(-10 + x,10 + y)
    baker_turtle.stamp()

    baker_turtle.goto(10 + x, -10+ y)
    baker_turtle.stamp()


make_cookie(10, 10)

for _ in range(100):
    make_cookie(
        random.randint(-h + 30, h -30),
        random.randint(-w + 30, w -30)
        )

turtle.done()


# Alternative way of making another cookie:
 #rp = random.randint(-100, 101)

# Draw outline of cookie
#baker_turtle.penup()
#baker_turtle.goto(-5 + rp, -30 + rp)
#baker_turtle.pendown()
#baker_turtle.circle(30)
#baker_turtle.penup()

# Add chips
#baker_turtle.color("black")

#baker_turtle.goto(0+ rp, 0 + rp)
#baker_turtle.stamp()

#baker_turtle.goto(10 + rp, 10)
#baker_turtle.stamp()

#baker_turtle.goto(-10 + rp, -10 + rp)
#baker_turtle.stamp()

#baker_turtle.goto(-10 + rp, 10 + rp)
#baker_turtle.stamp()
#baker_turtle.goto(10,-10)
#baker_turtle.stamp()

