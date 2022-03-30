import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

M = int(sys.stdin.readline())
inp = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(M):
    start = 1
    end = arr[-1]
    