N, X = map(int, input().split())
arr = [int(i) for i in input().split()]
result = []
for i in arr:
    if X > i: result.append(i)

print(*result)