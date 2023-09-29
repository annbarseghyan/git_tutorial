import sys

if len(sys.argv) < 1:
    print("Usage: fibonacci.py N")
    sys.exit(1)

def fib_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(sys.argv[1])

for i in range(n):
    print(fibonacci_recursive(i))

