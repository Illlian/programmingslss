# Parental bot
# Question 2
# Illia Nyshpor
# Date: 16.11.23

questions = [
    "Did you eat?",
    "Did you study?",
    "Did you do your laundry?",
    "Did you call grandma?"
]

ps = 0 

for question in questions:
    print(question)
    answer = input().lower().strip(",.?! ")
    if answer == "yes":
        ps += 1

    if ps < 1:
       print("I'm coming over")
    elif 1 <= ps > 3:
       print("Ok")
    elif ps >= 3:
       print("Good")    
