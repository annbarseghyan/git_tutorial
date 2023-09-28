import sys

if len(sys.argv) < 1:
    print("Usage: fibonacci.py N")
    sys.exit(1)

def fibonacci_rec(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

n = int(sys.argv[1])

for i in range(n):
    print(fibonacci_rec(i))

