# Jelly bean counter
# Illia Nyshpor
# 09.01.24

# Version 0.1
# Count and report on the percentage of red beans

from PIL import Image 

import colour_helper

jelly_bean_im  = Image.open("./Images/Jelly beans.jpg")

rp = []

for y in range(jelly_bean_im.height):
    for x in range(jelly_bean_im.width):
        cp = jelly_bean_im.getpixel((x, y))

        if colour_helper.pixel_to_name(cp) == "red":
            rp.append((x,y))

rp_count = len(rp)
tp = jelly_bean_im.width * jelly_bean_im.height
rp_percentage = rp_count / tp * 100

print(rp) 
print(rp_count)
print(f"{rp_percentage:.2f} %")          

jelly_bean_im.close()