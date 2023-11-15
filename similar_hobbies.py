# Similarity score practice 
# Question 1
# Illia Nyshpor
# Date: 14.11.23


first_hobbies = input(" What are your hobbies? ").lower().split()
second_hobbies = input(" What are your hobbies? ").lower().split()

ss = 0
# def double(bonus):
#     return bonus.strip(".,? ")

# hobbies = map(double, first_hobbies)
# hobbies_two = map(double, second_hobbies)





for hobbie in first_hobbies:
    if hobbie in second_hobbies:
        ss += 1
        

print(f"You have {ss} hobbies in common")