# Functions practice
# Illia Nyshpor
# Date: 24.11.23 

def  print_area_of_a_square(sidelength: float) ->  None:
	"""Calculates the area of a square.
	Results - units squared
	
	Params:
	sidelengh - length of one side of a square"""
	
	area = sidelength ** 2
	
	
	print(f"The area of a square with sidelength = {sidelength} is {area} square units")

print_area_of_a_square(12.2) 
print_area_of_a_square(13)  


def area_of_a_square(sidelength: float) -> float:
    """Returns the area of a square with given
    sidelength

    Params:

    sidelength - length of one side of a square
    """
    area = sidelength ** 2

    return area

print_area_of_a_square(12.2)
print_area_of_a_square(13)
# sum_areas = area_of_a_square(12.2) + area_of_a_square(13)
print(area_of_a_square(2))

print(print_area_of_a_square(2))


# Question 1

def stars(num_stars: int) -> str:
    """Return the same number of stars as you put in"""

    sr = "*" * num_stars

    return sr

print(stars(8))


# Question 2

def biggest_of_threee(num_one: int, num_two: int, num_three: int) -> int:
     
     if num_one > num_two and num_one > num_three:
          return num_one
     elif num_two > num_one and num_two > num_three:
          return num_two
     elif num_three > num_two and num_three > num_one:
          return num_three
     
print(biggest_of_threee(1, 2, 3))


# Question 3

def pyramid(num_st: int) -> str:
    st = "*"
    pr = 1
    for _ in range(num_st):
        print(st * pr)
        pr = pr + 1
           
pyramid(5)


# Question 4

def pyramid_mirror(num_st: int) -> str:
    on = " "
    st = "*"
    pr = 1
    ps = num_st - 1
    for _ in range(num_st):
        print(f"{on * ps}{st * pr}")
        pr = pr + 1
        ps = ps - 1
           
pyramid_mirror(5)