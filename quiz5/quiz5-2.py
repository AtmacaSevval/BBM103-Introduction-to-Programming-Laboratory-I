import sys
n = sys.argv[1]
n = int(n)
print('\n'.join(" " * (n - i - 1) + '*' * (2 * i + 1) for i in range(n)))
print('\n'.join(" " * (n - i - 1) + '*' * (2 * i + 1) for i in range(n-2,-1,-1)))
