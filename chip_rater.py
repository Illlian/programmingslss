# Chip rater
# illia Nyshpor
# Date: 02.11.23

# Interview people about their perception of the deliciousness of potato chips
# ask questions
# Give them an aggregate score

# Greet the user
print("Hi, please answer a few questions on the chip you just ate")

# Create a list of questions to ask
questions = [
    "How crispy is the chip on a scale from 1- 5 (5 being super crispy)?",
    "How would you rate the taste of the chip from 1-5 (5 being super tasty)?",
    "How would you rate the packaging from 1-5 (5 being the packaging looks amazing)"

]

# For every question in the list 
total_rating = 0

for question in questions:
    print(question)

  # Get the rating
    user_rating = int(input().strip(",.?! "))

  # Add the results to some total

    total_rating += user_rating

# Do some math (use the average score
average_rating = total_rating / len(questions)

# Print out the results
print(f"The average rating for this chip is: {average_rating:.2f}/5")
