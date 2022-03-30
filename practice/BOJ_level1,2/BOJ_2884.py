N, M = map(int, input().split())

M2 = (M - 45) % 60
if M - 45 < 0:
    N = (N - 1) % 24

print(N, M2)