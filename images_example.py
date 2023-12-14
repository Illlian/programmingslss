# Images and python
# Illia Nyshpor
# 11.12.23 / 14.12.23

from PIL import Image 

def pixel_to_name(pixel: tuple) -> str:
    red, green, blue = pixel 

    if red < 55 and blue < 55 and green > 140:
        return "green"
    else:
        return "colour unknown"

with Image.open("./Images/kid-green.jpg") as im:
    ih = im.height
    iw = im.width

    bg_im  = Image.open("./Images/beach.jpg")
    for y in range(ih):
        for x in range(iw):

            pixel = im.getpixel((x,y))
     
            if pixel_to_name(pixel) == "green":
                bg_pixel = bg_im.getpixel((x, y))

                im.putpixel((x, y), bg_pixel)

bg_im.close()

im.save("./Images/output.jpg")


# Image practice example
# from PIL import Image 
# with Image.open("./Images/kid-green.jpg") as im:
#    pixel = im.getpixel((0,0))
#    print(pixel)

#   mc = im.width // 2
#   pixel = im.getpixel((mc, mc))
#   print(pixel)

