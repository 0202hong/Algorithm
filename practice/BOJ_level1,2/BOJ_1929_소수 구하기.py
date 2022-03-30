import sys

N, M = map(int, sys.stdin.readline().split())

for i in range(N, M + 1):
    divide = True
    for j in range(2, int(i ** (1/2)) + 1):
        if i % j == 0:
            divide = False
            break
    
    if i != 1:
        if divide: print(i)