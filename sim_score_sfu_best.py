# SFUs Best - Similarity score
# Illia Nyshpor
# Date: 10.11.23

# Load data from a file
# "Read" it in a meaningful way
# Link our sim score algo to the data

# Open file
# Get the first line of data
# Create a "profile" of likews (fave places in sfu)
# For every line of data in the file
  # Convert the string to alist
  # for item in profile
    # if item in profile
    # increase the number of likes by 1
# Throw away the header 
# initialise the current sim score


with open("./data.csv") as f:
    f.readline()

profile = [
    "Bubble World",
    "Chef Hung",
    "Pizza Hut",
    "Guadalupe(MBC)",
    "Subway",
]

with open("./data.csv") as f:
    header = f.readline()

    for line in f:
         current_likes = line.split(",")

         name = current_likes[1]
         sim_score = 0

         for item in profile:
             if item in current_likes:
                 sim_score +=1

print(f"{name} - Score: {sim_score}")


