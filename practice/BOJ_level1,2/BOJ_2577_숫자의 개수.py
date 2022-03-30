import sys

result = 1
for _ in range(3):
    result *= int(sys.stdin.readline())

arr = [0 for _ in range(10)]
for res in str(result):
    arr[int(res)] += 1

print(*arr, sep = '\n')