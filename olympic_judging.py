# Question 2
# Illia Nyshpor
# Date: 03.11.23

print("Here, 5 judges will judge how well your Olimpic score is")

judges = ["Judge 1", "Judge 2", "Judge 3", 'Judge 4', "Judge 5"]

total_score = 0

average_rating = total_score / 50

for judge in judges:
    rating = float(input(f"{judge} gives you a score of: "))

    total_score += rating

average_rating = total_score / len(judges)

print(f"Your total Olimpic score is:{average_rating:.1f}/10 ")