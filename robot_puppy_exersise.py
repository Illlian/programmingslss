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
# print(rp_count)
# print(r)
# print(m)

# print(xv, yv)
# print(xr)
# print(yr)

bim.close()


# Proper solution
# Find the ball
from PIL import Image
# Open the image
ball_image = Image.open("./Images/red ball.jpeg")
red_pixel_locs = []
# Visit every pixel and find the red ones
for y in range(ball_image.height):
    for x in range(ball_image.width):
        r, g, b = ball_image.getpixel((x, y))
        if r > 200 and g < 70 and b < 70:
            red_pixel_locs.append((x, y))
x_coords = []
y_coords = []
for loc in red_pixel_locs:
    x_coords.append(loc[0])  # (x, y)
    y_coords.append(loc[1])
# Find the min and max of x and y
min_x = min(x_coords)
max_x = max(x_coords)
min_y = min(y_coords)
max_y = max(y_coords)
# for x_coord in x_coords:
#     if x_coord < min_x:
#         min_x = x_coord
#     if x_coord > max_x:
#         max_x = x_coord
print(min_x, max_x, min_y, max_y)
# Find the maximum x and maximum y
# Calculate the midpoint between the two
mid_x = min_x + (max_x - min_x) // 2
mid_y = min_y + (max_y - min_y) // 2
# Report the results
print(mid_x, mid_y)
# Put a crosshair at the coordinate in redball
ball_image.putpixel((mid_x, mid_y), (255, 255, 0))
ball_image.putpixel((mid_x + 1, mid_y), (255, 255, 0))
ball_image.putpixel((mid_x - 1, mid_y), (255, 255, 0))
ball_image.putpixel((mid_x, mid_y + 1), (255, 255, 0))
ball_image.putpixel((mid_x, mid_y - 1), (255, 255, 0))
ball_image.save("red_ball_result.jpg")
ball_image.close()