import sys

N = int(sys.stdin.readline())
arr = set(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline())
inp = list(map(int, sys.stdin.readline().rstrip().split()))

for i in inp:
    if i in arr:
        print(1)
    else:
        print(0)