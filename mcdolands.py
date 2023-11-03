# Question 3
# Illia Nyshpor
# Date: 03.11.23

print("I am here to take your order!")

total_price = 0

burger = input("Would you like a burger for $5? (yes/no) ")
if burger == "yes" or burger == "Yes":
    total_price += 5
fries = input("Would you like some fries for $3? (yes/no) ")
if fries == "yes" or fries == "Yes":
    total_price += 3
else:
    print("Sorry we could not help you! Thank you for visiting McDolands!")

print(f"Your total is: $ {total_price / 14 * 100:.2f}")

