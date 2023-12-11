# Images and python
# Illia Nyshpor
# 11.12.23

from PIL import Image 

with Image.open("./Images/kid-green.jpg") as im:

    pixel = im.getpixel((0,0))

    print(pixel)