import sys
n = sys.argv[1]
n = int(n)
num = n
def pattern(n,num):
    if n == 0:
        return
    print(" " * (n - 1) + "*" * (num - n + 1), end="\n")
    return pattern(n-1, num+1)

def pattern2(n1,num1):
    if n1 == 0:
        return
    print(" " * (n1 - num1 + 1) + "*" * (2 * n1 - 1), end="\n")
    return pattern2(n1 - 1, num1 - 2)

def ful(n,num):
    if n == 0:
        exit()
    pattern(n, num)
    pattern2(n - 1, num - 1)
    exit()
ful(n,num)
