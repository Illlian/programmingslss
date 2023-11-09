# Calculating similarity score
# Illia Nyshpor
# Date: 09.11.23

# Calculate the similarity score betwen two people

# Create two lists that represent the movies they like
# For every movie in the first list, if its in the second list, increase the simularity score by 1
#(increase similarity score if the movies are the same)
# print the results

first_person_movies = [
    "some movie 1",
    "some movie 2",
    "some movie 3",
    "some movie 4"
]

second_person_movies = [
    "random movie 1",
    "random movie 2",
    "some movie 1",
    "some movie 2",
    "random movie 3"
]

ss = 0

for movie in first_person_movies:
    if movie in second_person_movies:
        ss += 1

print(f"The similarity score between the two people is: {ss}")