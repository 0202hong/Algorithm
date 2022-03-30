import sys

N = int(sys.stdin.readline())

inp = []
for _ in range(N):
    inp.append(sys.stdin.readline().rstrip())

inp = list(set(inp))
inp.sort()
inp.sort(key = lambda x: len(x))

for i in inp:
    print(i)