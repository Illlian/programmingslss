# Format strings

We can evaluate inside of strings using f-strings
To create it we put an **f** before opening quote
```python
ff = input("What is your favourite food?")

print(f "Eugh i hate {ff}")
```

# String methods

[[Methods]] are functions we can use on [[Objects]]. 

String methods allow us to modify and work with strings.

Eg: We want to make all characters in a string lowercase.

```python
sy = "STOP SCREAMING"

print(sy.lower())   #lowercases the letters
```

##  `.lower()`


The .lower() method takes the string and converts the uppercase characters to lowercase

We can use .lower to help with [[Errors#Semantic errors Errors|errors]].


## `.upper()`

The .upper() method converts all lowercase letters into uppercase in a string


## `.strip(str)`

The .strip method removes characters from the beginning or end of the string.

```python
uf = input("How are you feeling? ")

if uf.lower().strip("!.,?") == "good":
   print("Cool")
```

## `.split(str)`

The .split() method splits the string into a [[Lists|list]], separating the string based on the characters you give it.

```python
gr = "stuff morestuff randomstuff"

gl = gr.split(" ")
```















