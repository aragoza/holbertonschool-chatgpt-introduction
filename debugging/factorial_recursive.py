#!/usr/bin/python3
import sys

def factorial(n):
    """
    Return the factorial of a non-negative integer n.

    n: non-negative integer
    return: factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read number from command line argument
num = int(sys.argv[1])
result = factorial(num)
print(result)
