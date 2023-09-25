# Chatbot
# Author: Illia Nyshpor
# Date: 21.09.23 / 25.09.23

#Greet the user
#Get the users name, store it in a variable
#Respond with the users name
#Ask for their fav food
#Respond with something appropriate

#Respond with something not too repetive
#Create a list of responces
#Chose one random from the list
#Print chosen responce

print("Hi!")
print("I am a crude chatbot. You can talk to me")
uname = input("What`s your name?")
print(f"Nice to meet you, {uname}")
ff = input(f"What is your favourite food {uname}?")

list_of_ff_resp = [
    f"You have a weird taste. {ff} is disgusting",
    "Sounds tasty",
    f"I also kinda like {ff}",
    "Nice",
    "Cool, i also like it!",
    "I approve of your choice"
]

import random
rr = random.choice(list_of_ff_resp)
print(rr)
