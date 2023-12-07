A function is a block of code that can be reused over and over again.

We can input data into the function. We can refer to the data as **parameters**.
We use the term **arguments** to describe the ACTUAL data that we put into a function.


```python
def area_of_a_sqyare(sidelength: float):  # sidelength is the parameter
	"""Calculates the area of a square.
	Results - units squared
	
	Params:
	sidelengh - length of one side of a square""""
	
	area = sidelength ** 2
	
	print(f"The area of a square with sidelength = {sidelength} is {area} square units")

area_of_a_square(12.2)  # 12.2 is the argument

```

## Functions with return values

We can call these functions , ***fruitful functions*** 
This term is not used in industry!

eg:
```python
def adder(x: int, y; int) -> None:
	"""Returns the sum of given numbers"""
	sum = x + Y

	return sum
adder(10, 2)
print(adder(10,12)) # printa the value 12
```

The *return* keyword does two things in a function:
1. Stops the function
2. If there is a value after return, it sends the value back to where the function is called

```python
def linear_search(l: list, item: any) -> int:
	"""Search through a list and if found returns the index of the first occurance item
	Returns: if index not found return -1 """

	counter = 0
	
	for thing in l:
		if thing == item:
			return counter
		counter += 1
	return -1
```

## Recursion

Recursion is an *elegant* way to repeat a pattern 

Fractals are examples of patterns that can be described recursively 

A recursive function must have 3 parts:
1. A function
2. The function should call itself
3. A base case  (where a function stops calling itself)

### Factorials and recursion

```
0! =1
1! = 1

2! = 1*2
2! = 1!*2

3! = 1*2*3
3! = 2!*3*
```

