import sys

tmp = sys.stdin.readline()
inp = list(map(int, sys.stdin.readline().split()))

max_inp = max(inp)

for i in range(len(inp)):
    inp[i] = inp[i] / max_inp * 100


print(sum(inp) / len(inp))