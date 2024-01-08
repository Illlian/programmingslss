# Image problems
# Illia Nyshpor
# Date: 18.12.23

# Question 1
from PIL import Image

import colour_helper

# Test
light_pixel = (255, 255, 255)
light_gray = (128, 128, 128)
dark_gray = (127, 127, 127)
dark_pixel = (0, 0, 0)

print(colour_helper.is_light(colour_helper.light_pixel))  # True
print(colour_helper.is_light(colour_helper.light_gray))  # True
print(colour_helper.is_light(colour_helper.dark_gray))  # False
print(colour_helper.is_light(colour_helper.dark_pixel))  # False



# Question 1
# Change image to black and white
with Image.open("./Images/catto.png") as im:
     ih = im.height
     iw = im.width

     for y in range(ih):
        for x in range(iw):

            pixel = im.getpixel((x,y))
     
            if colour_helper.is_light(pixel) == True:
                im.putpixel((x,y), colour_helper.light_pixel)
            else:
                im.putpixel((x,y), colour_helper.dark_pixel)

im.save("./Images/output.jpg")

im.close()



# Question 2
# Change image into gray
def picture_to_grayscale(filename: str) -> None:
    """Convert a given picture to grayscale"""

    # Open up the image
    with Image.open(f"./Images/{filename}") as im:
        # Visit every pixel
        ih = im.height
        iw = im.width

        for y in range(ih):
            for x in range(iw):

                pixel = im.getpixel((x, y))
              
                # Take that pixel and convert it to gray
                gray_pixel = colour_helper.pixel_to_grayscale(pixel)

                im.putpixel((x, y), gray_pixel)
        
        # Save the image
        im.save("./Images/grayscale.jpg")
        
picture_to_grayscale("catto.png")
