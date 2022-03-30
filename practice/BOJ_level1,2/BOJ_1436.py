import sys

inp = int(sys.stdin.readline())

def func(n):
    num = 665
    while n != 0:
        num += 1
        if '666' in str(num):
            n -= 1
    
    return num

print(func(inp))