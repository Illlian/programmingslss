# Chatbot
# Author: Illia Nyshpor
# Date: 21.09.23 / 25.09.23 / 28.09.23

#Greet the user
#Pause in between lines of dialogue
#Get the users name, store it in a variable
#Respond with the users name
#Ask for their fav food
#If they answer pasta, respond to something related

#Respond with something appropriate
#Respond with something not too repetive

#Create a list of responces
#Chose one random from the list
#Print chosen responce

import random
import time

print("Hi!")
time.sleep(1)
print("I am a crude chatbot. You can talk to me")
time.sleep(0.5)
uname = input("What`s your name? ")
print(f"Nice to meet you, {uname}")
time.sleep(1)
ff = input(f"What is your favourite food {uname}? ")


list_of_ff_resp = [
    f"You have a weird taste. {ff} is disgusting",
    "Sounds tasty",
    f"I also kinda like {ff}",
    "Nice",
    "Cool, i also like it!",
    "I approve of your choice"
]
rr = random.choice(list_of_ff_resp)

if ff == "pasta" or ff == "Pasta":
    print("Pasta sounds nice")
elif ff == "mashed potatoes" or ff == "Mashed Potatoes":
    print("You are a God!")
elif ff == "sushi" or ff == "Sushi":
    print("Cute!")
    time.sleep(0.5)
    print("Japan has a lot of tasty food")
else:
    time.sleep(1)
    print(rr)
