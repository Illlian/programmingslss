# Bubble tea popularity algoritm
# illia Nyshpor
# Date: 27.10.23 / 30.10.23

# ask 5 users about thie favourite bubble tea place and print out the results

# Ast the user about their favourite bubble tea place

# Counting algoritm
# Options: Coco Chatime SunTea Xing Fu Tang Bubble Queeen
# If they say one of the options the number increases by one
# Print out the results
 
NUM_RESPONDDENTS = 2

coco_likes = 0  
Chatime_likes = 0
suntea_likes = 0
Xian_Fu_Tang_likes = 0
bbqueen = 0

for _ in range(NUM_RESPONDDENTS):

    print("What is your favourite bubble tea store? ")
    fb = input().strip(",.?! ").lower

    if fb == "coco":
        coco_likes = coco_likes +1
    elif fb == "Chatime":
        Chatime_likes += 1
    elif fb == "suntea":
        suntea_likes += 1
    elif fb == "Xing Fu Tang":
        Xian_Fu_Tang_likes += 1
    elif fb == "Bubble Queeen":
        bbqueen =+ 1


print(f"Coco likes: {coco_likes}")
      
print (f"Chatime likes: {Chatime_likes}")

print(f"Suntea likes: {suntea_likes}")

print(f"Xian Fu Tang likes: {Xian_Fu_Tang_likes}") 

print(f"Bubble Queeen: {bbqueen}")
 

