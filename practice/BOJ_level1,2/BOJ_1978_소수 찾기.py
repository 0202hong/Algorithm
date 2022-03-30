import sys

N = int(sys.stdin.readline())
arr = [int(i) for i in sys.stdin.readline().split()]

cnt = 0
for i in arr:
    divide = True
    for j in range(2, int(i ** (1/2)) + 1):
        if i % j == 0:
            divide = False
            break
    
    if i != 1:
        if divide: cnt += 1

print(cnt)