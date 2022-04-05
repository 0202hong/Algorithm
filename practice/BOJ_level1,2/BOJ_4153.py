import sys

while True:
    A, B, C = map(int, sys.stdin.readline().rstrip().split())

    if A == 0 and B == 0 and C == 0:
        break
    arr = sorted([A, B, C])
    
    if arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2:
        print('right')
    else:
        print('wrong')