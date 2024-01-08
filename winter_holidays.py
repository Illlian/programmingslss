# Winter holidays review
# Illia Nyshpor
# 08.01.24


import random

def winter_holiday(gb: str) -> str:
    """Summary  of winter holidays 
    
    Parameters: 
    choose good or bad event
    
    Returns:
    random event during the holidays"""

    ge = ["Got a  new phone", "Went book shopping with a friend", "Dyed my hair a different colour"]
    be = ["Did not get to travel", "Spent too much time indoors", "Was not left alone to relax by my family"]

    if gb.lower().strip(",.?!") == "good":
        good = random.choice(ge)
        return good
    elif gb.lower().strip(",.?!") == "bad":
        bad = random.choice(be)
        return bad


def main() -> None:
    print(winter_holiday("good"))

    print(winter_holiday("bad"))

if __name__ == "__main__":
    main()

