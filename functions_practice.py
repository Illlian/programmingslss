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


      

      
      