import sys

while True:
    inp = sys.stdin.readline().rstrip()

    if inp == '0': break
    else:
        if inp == inp[::-1]:print('yes')
        else:print('no')