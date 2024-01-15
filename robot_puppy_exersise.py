# Question 1
# Illia Nyshpor
# 12.01.24

# Code that calculates the center location of the red ball (x, y coordinates)

from PIL import Image 
import colour_helper


bim = Image.open("./Images/Red Ball.jpeg")

rp = []
xr = []
yr = []

for y in range(bim.height):
    for x in range(bim.width):
        cp = bim.getpixel((x, y))

        if colour_helper.pixel_to_name(cp) == "red ball":
            rp.append((x,y))
            xr.append(x)
            yr.append(y)

rp_count = len(rp)

r = (sum(max(rp)) - sum(min(rp))) // 2

xv = (max(xr) - min(xr)) 
yv = (max(yr) - min(yr)) 

# Test
# xv = 148
# yv = 61

m = (xv, yv)

for m in rp:
    if rp == m:
        print(m)
        break

        
# print(max(rp))
print(rp_count)
print(r)
print(m)

# print(xv, yv)
# print(xr)
# print(yr)

bim.close()