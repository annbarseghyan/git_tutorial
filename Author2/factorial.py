import sys

if len(sys.argv) < 1:
    print("Usage: factorial.py N")
    sys.exit(1)

def factorial_recursive_anna(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

n = int(sys.argv[1])
print(factorial_recursive(n))
