# World travel bot
# Illia Nyshpor
# Date: 03.11.23 / 06.11.23

name = input("Hi, what is your name? ")
print(f"Welcome {name}, i just wnted to ask about your travelling history")

continents = ["Have you ever been to Asia?",
              "Have you ever been to Europe",
              "Have you ever been to North America?",
              "Have you ever been to South America?",
              "Have you ever been to Australia?",
              "Have you ever been to Africa?",
              "Have you ever been to Antarctica?"
              ]

num_continents = 0

for continent in continents:

    print(continent)
    total = input().lower

    if total == "yes":
      num_continents +=1
      print(num_continents)
        
print(f"Cool, you have visites {num_continents}/7 continents.")


