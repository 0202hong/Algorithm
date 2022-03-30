import sys

N = int(sys.stdin.readline())

for _ in range(N):
    inp = sys.stdin.readline()

    sum = 0
    score = 1
    for i in inp:
        if i == 'O':
            sum += score
            score += 1
        else:
            score = 1
    
    print(sum)