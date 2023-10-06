# Food suggestion bot
# Illia Nyshpor
# Date: 06.10.23

# A bot that ask the user about their fav food 
# Identifies the type of the food 
# Offers a suggestion or a restaurant based on that information


# Introduction to the bot
# Ask for the users fav food

# If they answer with an italian dish, suggest an italian restaurant
# List all the italian dishes

# Add one more type of food and suggestion


import random
import time

print("Hi")
time.sleep(1)
print("I can suggest you a restaurant")
time.sleep(1)
ff = input("What is your favourite food? ")

itf = ["pizza", "pasta", "tiramisu"]
jpf = ["sushi", "mochi", "kimchi"]

if ff.lower().strip(",.?! ") in itf:
    print("You probably like italian food")
    time.sleep(1)
    print("You can go to [random italian restaurant name]")
    time.sleep(1)
    print("Here is the adress [random adress]")


elif ff.lower().strip(",.?! ") in jpf:
    print("You probably like japanese food")
    time.sleep(1)
    print("You can go to [random japanese restaurant name]")
    time.sleep(1)
    print("Here is the adress [random adress]")
else:
    print("I have no idea what it is or where to find it")

time.sleep(1)
print("i have nothing else to help you. You can leave")

