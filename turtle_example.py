# Turtle example
# Illia Nyshpor
# Date: 21.11.23

# Create turtle
# Get some instructions from the user
# Based on those instructions move the turtle on the screen

import turtle

TMAGNITUDE = 20

vo = turtle.Turtle()

print("""To give commands, type:
      W to go forward
      A to go left
      D to go right
      S to go backward
      Type stop to stop""")

done = False

while not done:

    command = input("Where should i go? ").strip(",.?! ").lower()

    if command == "w":
        vo.forward(TMAGNITUDE)
    elif command == "a":
        vo.left(90)
    elif command == "d":
        vo.right(90)
    elif command == "s":
        vo.backward(TMAGNITUDE)
    elif command == "stop":
        done = True

