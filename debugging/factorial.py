#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        sys.exit(1)
    elif n == 0:
        return 1
    else:
        result = 1
        while n > 1:
            result *= n
            n = n - 1
        return result

if len(sys.argv) != 2:
    print("Usage: python script_name.py <number>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("Error: Input must be an integer.")
    sys.exit(1)

print(factorial(num))
