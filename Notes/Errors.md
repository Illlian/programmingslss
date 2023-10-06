# Syntax errors

These types of errors are ones the occur what you run your code and then it breaks.

They are relatively easy to spot and fix.

Syntax errors occur when we do not follow the rules of the language completely.

# Semantic errors

Semantic errors occur when our code does not MEAN what we intended it to mean.

These errors are a lot more challenging to spot fix.

eg
```python
ur = input("Do you like to eat food?")

if ur == "yes":
     print(" Congratulations! You are a human"
else: 
	print("You are probably a robot")	
```

The problem with the code above is subtle. The writer intends for EVERY ANSWER of YES to be put into the block.

One way to solve the problem we can use [[Strings#String methods Strings|string methods]]

We can use .lower() to fix this error

```python
ur = input("Do you like to eat food?")

if ur .lower() == "yes":
     print(" Congratulations! You are a human"
else: 
	print("You are probably a robot")
```	
