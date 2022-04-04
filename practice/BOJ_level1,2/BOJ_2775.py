import sys

T = int(sys.stdin.readline().rstrip())

apartment = [[0 for _ in range(14)] for _ in range(15)]

apartment[0] = [i for i in range(1, 15)]


floor = 0
for apart in apartment[1:]:
    for i in range(14):
        apart[i] = sum(apartment[floor][:i + 1])
    floor += 1

for i in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    print(apartment[k][n - 1])