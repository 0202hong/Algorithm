import sys

while True:
    try:
        inp1, inp2 = map(int, sys.stdin.readline().split())
        print(f'{inp1 + inp2}')
    except:
        break
