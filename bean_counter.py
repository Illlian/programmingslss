# Jelly bean counter
# Illia Nyshpor
# 09.01.24

# Version 0.1
# Count and report on the percentage of red beans

# Version 0.2
# Count and report on the percentage of green beans

# Version 0.3
# Count and report on the percentage of yellow and blue beans

RED_PIXEL  = (160,0,0)
GREEN_PIXEL = (0, 160, 0)
YELLOW_PIXEL = (220, 183, 3)
BLUE_PIXEL = (20, 40, 160)
DARK_BLUE_PIXEL = (0, 0, 220)

from PIL import Image 

import colour_helper

jelly_bean_im  = Image.open("./Images/Jelly beans.jpg")

rp = []
gp = []
yp = []
bp = []
dbp = []

for y in range(jelly_bean_im.height):
    for x in range(jelly_bean_im.width):
        cp = jelly_bean_im.getpixel((x, y))

        if colour_helper.pixel_to_name(cp) == "red":
            rp.append((x,y))
        elif colour_helper.pixel_to_name(cp) == "jelly bean green":
            gp.append((x, y))
        elif colour_helper.pixel_to_name(cp) == "yellow":
            yp.append((x, y))    
        elif colour_helper.pixel_to_name(cp) == "blue":
            bp.append((x, y)) 
        elif colour_helper.pixel_to_name(cp) == "dark blue":
            dbp.append((x, y))        


oimwidth = jelly_bean_im.width
oimheight = jelly_bean_im.height

pixel_map = Image.new("RGB", (oimwidth, oimheight))
for pixel_loc in dbp:
    pixel_map.putpixel(pixel_loc, DARK_BLUE_PIXEL)

for pixel_loc in bp:
    pixel_map.putpixel(pixel_loc, BLUE_PIXEL)
pixel_map.save("./Images/Blue_pixel_map.jpg")

for pixel_loc in rp:
    pixel_map.putpixel(pixel_loc, RED_PIXEL)
pixel_map.save("./Images/pixel_map.jpg")

for pixel_loc in gp:
    pixel_map.putpixel(pixel_loc, GREEN_PIXEL)
pixel_map.save("./Images/pixel_map.jpg")

for pixel_loc in yp:
    pixel_map.putpixel(pixel_loc, YELLOW_PIXEL)

pixel_map.save("./Images/pixel_map.jpg")
pixel_map.close

rp_count = len(rp)
gp_count = len(gp)
yp_count = len(yp)
bp_count = len(bp)
dbp_count = len(dbp)

tp = jelly_bean_im.width * jelly_bean_im.height
rp_percentage = rp_count / tp * 100

tp = jelly_bean_im.width * jelly_bean_im.height
gp_percentage = gp_count / tp * 100

tp = jelly_bean_im.width * jelly_bean_im.height
yp_percentage = yp_count / tp * 100

tp = jelly_bean_im.width * jelly_bean_im.height
bp_percentage = bp_count / tp * 100

tp = jelly_bean_im.width * jelly_bean_im.height
dbp_percentage = dbp_count / tp * 100

# print(rp) 
# print(rp_count)
print(f"Red pixels: {rp_percentage:.2f} %")

# print(gp_count)
print(f"Green pixels: {gp_percentage:.2f} %") 

# print(yp_count)
print(f"Yellow pixels: {yp_percentage:.2f} %") 

#print(bp_count)
print(f"Blue pixels: {bp_percentage:.2f} %") 

print(f"Dark blue pixels: {dbp_percentage:.2f} %") 
jelly_bean_im.close()