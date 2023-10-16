# Star Wars Bot
# Illia Nyshpor
# 16.10.23

# create a bot that decides if th euser will join the dark or light side

import time

print("Welcome!")
time.sleep(1)
print("You have to answer a few questions to test if you are suitable to join the dark side.")
time.sleep(1)

ac = input("Question 1: Do you like capes? ")
time.sleep(1)
print("Good")
time.sleep(1)
acl = input("Question 2: Do you like the colour red? ")    

if ac.lower().strip(",.?! ") == "yes" or acl.lower().strip(",.?! ") == "yes":
    time.sleep(2)
    print("*Drumroll*")
    time.sleep(1)
    print("welcome to the Dark Side")

else:
    time.sleep(2)
    print("Sorry, you do not meet the requirements to join the Dark Side")
    time.sleep(1)
    print("..but you are more than welcome to join the Light Side instead")
    time.sleep(1)
    print("everybody is allowed to join them.")
    time.sleep(1)
    print("Good luck!")
   