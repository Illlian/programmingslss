# Colour Helper
# Functions that help wither colours


light_pixel = (255, 255, 255)
light_gray = (128, 128, 128)
dark_gray = (127, 127, 127)
dark_pixel = (0, 0, 0)


def is_light(pixel: tuple) -> bool:
    """Returns True if the pixel is a "light" pixel

    Params:
        pixel - 3-tuple of values r, g, b

    Returns:
        True if the pixel is a light pixel
        False if a dark pixel
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = (red + green + blue) / 3

    if average >= 128:
        return True
    else:
        return False
    


def pixel_to_grayscale(pixel: tuple) -> tuple:
    """Return a gray version of the given pixel"""
    red, green, blue = pixel

    gray = int(red * 0.3 + green * 0.59 + blue * 0.11)

    return (gray, gray, gray)




def pixel_to_name(pixel: tuple) -> str:
    
    red, green, blue = pixel 

    if red < 55 and blue < 55 and green > 130:
        return "green"
    elif red > 170 and blue < 60 and green < 60:
        return "red"
    else:
        return "colour unknown"
    

# print(pixel_to_name((180, 3, 2)))
# print(pixel_to_name((255, 255, 255)))