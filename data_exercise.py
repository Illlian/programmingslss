from pathlib import Path


# File Exercises
# Author: illia Nyshpor
# Date: 16.11.23

"""Instructions:

Put this file in your programming folder.
Download the data-example.csv file and put it in this same folder.
For each problem, design a solution.
Each part builds on the previous step, so don't skip any.
You can refer to the work that we did last day for any hints.
Do not use any generative AI for the solutions."""

# Since our file has some symbols in it, this is the most
# effective way at opening up the file.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()

# Note that I've set the encoding parameter to "utf-8"

# --- Problems


# Problem 1:
# Open the file and print the contents of the second line in the file.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    second_line = f.readline()
    print(second_line)

# Problem 2:
# Good! Now that you've done that, open the file, and print out every line of data.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()

    for line in f:
        print(line)

# Problem 3:
# If you've made it this far, well done. Next task:
# Convert that line of data into a list.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()

    for line in f:
        datalist = line.split(",")

# Problem 4:
# Give yourself a pat on the back.
# See if you can count how many people like "Chicken Adobo" as their
# favourite food.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    chicken_people = 0

    for line in f:
        datalist = line.split(",")

        food = datalist[1]
   
        if food == "Chicken Adobo":
          chicken_people += 1
    
    print(f"{chicken_people} people like chicken adobo")

# Problem 5:
# You should have gotten four people for the last problem. If not,
# see if why your code doesn't work.
# Else, you can move on to this part, which is, find out how many
# people have the first letter of their first name start with "A".

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    names = 0

    for line in f:
        datalist = line.split(",")

        if f.readline(1) == "A":
            names += 1

    print(f"{names} peole have their name start with an A")

    
# Problem 6:
# 19 people! Excellent. How many people come from Guangzhou?

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    live = 0

    for line in f:
        datalist = line.split(",")
   
        city = datalist[4].rstrip()
       

        if city == "Guangzhou":
          live += 1
    
    print(f"{live} people are from Guangzhou ")


# Problem 6:
# Just one is from Guangzhou! Alright, last one. How many people have a credit card
# number that is even. There are a couple of ways to solve this.
# You can either do this with the string or with the int.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    credit_number = 0

    for line in f:
        datalist = line.split(",")

        number = datalist[3]

        evenumber = int(number[11])

        if evenumber // 2:
            credit_number += 1
    print(f"{credit_number} people have an even credit card")

        
# Problem 7:
# Sorry, no answer for the above one. This one is a challenge question.
# Can you design a way to find the most popular food?

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    ff = 0


    for line in f:
        datalist = line.split(",")

        food = datalist[1]
        # ages = [5, 12, 17, 18, 24, 32]

        #print(food)

        

  
        # for item in food:
        #     def myFunc(x):
        #      if x == item:
        #       return False
        #     ff_items = filter(myFunc, food) 
        #     print(ff_items)    


# adults = filter(myFunc, ages)


        