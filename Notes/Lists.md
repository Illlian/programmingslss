In python lists are a collection of items
We store values inside of lists
The values of the items can be of different [[Types]]
**Order matters** in a list

# Creating a list
To make a list, we use brackets \[\] to surround our list
We separate the individual items with commas
eg
```python
some_list = ["Jimmy", "Sara", "Frederique"]

```

# Access elements in the list
We can access the individual things in a list using bracket notation
Access eg:
```python
some_list[1]           #"Sara"
some_list[0]           #"Jimmy"  
some_list[-1].         #"Frederique", from the end
```
Inside the brackets, we give the *index* of the item we want
Python uses 0-index counting, which means we start counting at 0


## 2- Dimensional lists

All the lists used so far were **one dimensional**

```python
some_list = ["blue", "red", "green"]
```

List can be **two dimensional** 
These are multiple lists inside a bigger list

```python
some_2d_list = [
	[1,2,3], 
	[4,5,6],
	[7,8,9]
]

some_2d_list[0] [0] # -> 1
some_2d_list[0] [1] # -> 2
        #   |    |
        #  row  column
```
## Tuples

**Tuples** are like lists, except for one thing:
They are immutable (unchangeable)


It is not possible to change the contents of a tuple
Tuples have some performance benefits

eg:
```python
some_tuple = (1,2,3,4)
```


### Images and tuples

The basic unit of measurements in an image is a pixel
The pixel information is stored in a tuple of three values (3-tuple)

The 3-tuple tells us for ONE PORTION of an image what the RED, GREEN and BLUE values are

```
Red - (255, 0, 0)
Green - (0, 255, 0)
Blue - (0, 0, 255)

red, green, blue in this order

range from 0 - 255
```
