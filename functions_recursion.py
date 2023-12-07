# Recursions practice
# illia Nyshpor
# Date: 07.12.23

def factorial( n: int) -> int:
    """Return the nth factorial"""

    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return factorial(n-1) * n
    
print(factorial(3))


def fib(n: int) -> int:
    """Returns the nth Fibonacci number"""

    if n in [1,2]:
        return 1
    elif n> 2:
        return fib(n-1) + fib(n-2)
    
print(fib(3))
