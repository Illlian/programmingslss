# Image problems
# Illia Nyshpor
# Date: 18.12.23

# Question 1
from PIL import Image

def is_light(pixel: tuple) -> bool:
    """A fuction that determines 
    weather a pixel is light or dark"""

    red, green, blue = pixel

    if (red + green + blue) / 3 >= 128:
        return True
    else:
        return False

# Test
light_pixel = (255, 255, 255)
light_gray = (128, 128, 128)
dark_gray = (127, 127, 127)
dark_pixel = (0, 0, 0)

print(is_light(light_pixel))  # True
print(is_light(light_gray))  # True
print(is_light(dark_gray))  # False
print(is_light(dark_pixel))  # False



# Question 2
with Image.open("./Images/catto.png") as im:
     ih = im.height
     iw = im.width

     for y in range(ih):
        for x in range(iw):

            pixel = im.getpixel((x,y))
     
            if is_light(pixel) == True:
                im.putpixel((x,y), light_pixel)
            else:
                im.putpixel((x,y), dark_pixel)

im.save("./Images/output.jpg")