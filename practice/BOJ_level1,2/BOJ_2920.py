import sys

inp = list(map(int, sys.stdin.readline().split()))

tmp = [i for i in range(1, 9)]

if inp == tmp:
    print('ascending')
elif inp == sorted(tmp, reverse = True):
    print('descending')
else:
    print('mixed')