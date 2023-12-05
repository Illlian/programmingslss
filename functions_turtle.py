# Functions with turtle
# Illia Nyshpor
# Date: 28.11.23 / 04.12.23

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

# for i in range(20):
#    draw_square(squared(i))


# Recursive function for drawing trees

def draw_tree(level: int, height: int) -> None:
    """A recursion function that draws a tree with the initial given height
      """
    
    if level > 0:
        lewis.forward(height)
        lewis.left(39)
        draw_tree(level - 1, height / 1.5)

        lewis.right(39*2)
        draw_tree(level - 1, height / 1.5)
        lewis.left(39)
        lewis.back(height)

    else:
        oc = lewis.color()
        lewis.color("green")
        lewis.stamp()
        lewis.color(oc[0])

# lewis.left(90) --> the same thing as the line below
lewis.setheading(90)
# lewis.hideturtle()
lewis.speed(0)
lewis.width(4)
lewis.color("brown")
lewis.shape("arrow")




def draw_fancy_tree(level: int, height: int) -> None:
    """A recursion function that draws a tree with the initial given height
      """
    
    if level > 0:
        lewis.forward(height)

        #lewis.forward(39)
        draw_fancy_tree(level - 1, height / 1.5)
        
        lewis.left(39)
        draw_fancy_tree(level - 1, height / 1.5)
        
        lewis.right(39*2)
        draw_fancy_tree(level - 1, height / 1.5)
        lewis.left(39)
        

        lewis.back(height)

    else:
        oc = lewis.color()
        lewis.color("green")
        lewis.stamp()
        lewis.color(oc[0])


lewis.setheading(90)
lewis.speed(0)
lewis.width(4)
lewis.color("brown")
lewis.shape("arrow")

draw_fancy_tree(4, 150)

turtle.done()