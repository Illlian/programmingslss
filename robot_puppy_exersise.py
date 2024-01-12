# Question 1
# Illia Nyshpor
# 12.01.24

# Code that calculates the center location of the red ball (x, y coordinates)

from PIL import Image 
import colour_helper

bim = Image.open("./Images/Red Ball.jpeg")

rp = []

for y in range(bim.height):
    for x in range(bim.width):
        cp = bim.getpixel((x, y))

        if colour_helper.pixel_to_name(cp) == "red ball":
            rp.append((x,y))

rp_count = len(rp)
m = rp_count // 4

print(rp)
print(rp_count)
print(rp[m])

bim.close()