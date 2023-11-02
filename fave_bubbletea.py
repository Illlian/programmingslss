# Bubble tea popularity algoritm
# illia Nyshpor
# Date: 27.10.23 / 30.10.23

# ask 5 users about thie favourite bubble tea place and print out the results

# Ast the user about their favourite bubble tea place

# Counting algoritm
# Options: Coco Chatime SunTea Xing Fu Tang Bubble Queeen
# If they say one of the options the number increases by one
# Print out the results
 
NUM_RESPONDENTS = 5

coco_likes = 0  
chatime_likes = 0
suntea_likes = 0
xingfutang_likes = 0
bbqueen_likes = 0
other_likes = 0

for _ in range(NUM_RESPONDENTS):

    print("What is your favourite bubble tea store? ")
    fb = input().strip(",.?! ").lower()

    if fb == "coco":
        coco_likes = coco_likes +1
    elif fb == "chatime":
        chatime_likes += 1
    elif fb == "suntea":
        suntea_likes += 1
    elif fb == "xing fu tang":
        xingfutang_likes += 1
    elif fb == "bubble queeen":
        bbqueen_likes += 1
    else:
        other_likes +=1


coco_percentage = coco_likes / NUM_RESPONDENTS * 100
chatime_percentage = chatime_likes / NUM_RESPONDENTS * 100
suntea_percentage = suntea_likes / NUM_RESPONDENTS * 100
xingfutang_percentage = xingfutang_likes / NUM_RESPONDENTS * 100
bbqueen_percentage = bbqueen_likes / NUM_RESPONDENTS * 100
other_percentage = other_likes / NUM_RESPONDENTS * 100


print(f"Coco likes: {coco_likes}| {coco_percentage:.2f}%")     
print (f"Chatime likes: {chatime_likes}| {chatime_percentage:.2f}%")
print(f"Suntea likes: {suntea_likes}| {suntea_percentage:.2f}%")
print(f"Xian Fu Tang likes: {xingfutang_likes} | {xingfutang_percentage:.2f}%") 
print(f"Bubble Queeen: {bbqueen_likes}| {bbqueen_percentage:.2f}%")
print(f"Other Likes: {other_likes} | {other_percentage:.2f}%")


