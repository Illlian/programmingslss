---
tags:
  - programming
  - notes
  - y2023
  - programming-level-1-2
  - slss
---
# Recommendation systems
## Popularity and "Likes"

This type of paradigm makes a suggestion based on how many people "like" this thing.

One prime example of this is the like button(heart) in Instagram,
When someone clicks on the button, Instagram records it somewhere alongside of other data, like **demographic** and **psychographic** information.
With this information they might suggest to other users similar to you, products that you like.

The popularity likes paradigm is implemented in Favourite Bubble Tea activity

## N-Point Rating system

N-point rating systems are used by many services, particularly Amazon. 

This paradigm provides more granular information. Buyers are asked to rate the product on a 5-point scale. All the ratings are put together and the score is given out of five stars.

## Similarity score
Amazon, Meta, Tiktok, all use similarity scores to help drive and keep users on the platform

Eg:
Amazon
someone likes("random stuff", "more random stuff", "even more stuff")
someone else likes("the same random stuff", "slightly different stuff")
another person likes("different random stuff")

Similarity scores indicate how similar two people ate to each other
The first two people have a higher similarity score, since they like the same stuff

