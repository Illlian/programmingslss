# Semester evaluator bot
# Illia Nyshpor
# Date: 06.11.23

print("Hi, I am here to give a rating to your semester.")
cources = int(input("How many cources are you taking this semester? "))

rating_cources = 0
num_cources = 0

for i in range (cources):
    rating = float(input(f"How do you rate your cource {num_cources +1} out of 5? "))
    rating_cources += rating / cources
    num_cources = num_cources +1


if rating_cources < 1:
    print(f"Your overall score is {rating_cources :.1f} /5, Ouch")
elif 3 > rating_cources > 1:
    print(f"Your overall score is {rating_cources:.1f} /5, Not a bad semester")
elif rating_cources > 3:
    print(f"Your overall score is {rating_cources:.1f} /5, Glad to hear that")
