# Semester evaluator bot
# Illia Nyshpor
# Date: 06.11.23

print("Hi, I am here to give a rating to your semester.")
cources = int(input("How many cources are you taking this semester? "))

rating_cources = 0
num_cources = 0

for i in range (cources):
    rating = float(input("How do you rate cource out of 5? "))
    rating_cources += rating / cources


if rating_cources < 1:
    print(f"Your overall score is {rating_cources :.1f}, Ouch")
elif 3 > rating_cources > 1:
    print(f"Your overall score is {rating_cources:.1f}, Not a bad semester")
elif rating_cources > 3:
    print(f"Your overall score is {rating_cources:.1f}, Glad to hear that")
