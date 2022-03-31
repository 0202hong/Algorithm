N, M = map(int, input().split())

L, G = 0, 0
for i in range(1, min(N, M) + 1):
    if N % i == 0 and M % i == 0:
        G = i
L = int(N * M / G)
print(G)
print(L)
