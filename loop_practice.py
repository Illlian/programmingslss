# loop practice
# Illia Nyshpor
# Date: 10.10.23

# Create a list of groceries
# Print it out in a pretty way
#  eg  * item
#      ------
#      * item2
#      -------    

# Create a pyramid using a for loop
# *
# **
# ***
# ****
# *****

# Create a new years countdown
# Starts at ten and counts down to zero
# Print happy new year

import time
gr = ["Hot wheels", "lego", "ice cream"]

for item in gr:
     print(f"* {item}")
     print("  ---")


st = ["*", "**", "***", "****"]

for pl in st:
     print(pl)


numb = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1,] 

for im in numb:
     time.sleep(1)
     print(im)
print("It is not New Year yet, calm down!")