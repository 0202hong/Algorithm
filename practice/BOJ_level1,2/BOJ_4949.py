import sys

while True:
    inp = sys.stdin.readline().rstrip()

    if inp == '.': break

    arr = []
    balance = True
    for i in inp:
        if i == '(' or i == '[':
            arr.append(i)
        elif i == ')':
            if len(arr):
                if arr.pop() != '(': balance = False
            else: balance = False
        elif i == ']':
            if len(arr):
                if arr.pop() != '[': balance = False
            else: balance = False
        
    if balance: print('yes')
    else : print('no')
        