# Images and python
# Illia Nyshpor
# 11.12.23 / 14.12.23

from PIL import Image 

with Image.open("./Images/kid-green.jpg") as im:

    ih = im.height
    iw = im.width

    for y in range(ih):
        for x in range(iw):

            pixel = im.getpixel((x,y))
            print(x, y, pixel)



# Image practice example
# from PIL import Image 
# with Image.open("./Images/kid-green.jpg") as im:
#    pixel = im.getpixel((0,0))
#    print(pixel)

#   mc = im.width // 2
#   pixel = im.getpixel((mc, mc))
#   print(pixel)

