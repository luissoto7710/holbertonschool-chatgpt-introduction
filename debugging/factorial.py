#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) < 2:
    print("Usage: {} <integer>".format(sys.argv[0]))
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Please provide an integer.")
    sys.exit(1)

f = factorial(n)
print(f)