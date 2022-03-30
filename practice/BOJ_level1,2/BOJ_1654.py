import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

inp = []
for _ in range(n):
    inp.append(int(sys.stdin.readline().rstrip()))

start = 0
end = max(inp)
mid = (start + end) // 2

result = 0
while (start <= end):
# for _ in range(5):
    sum = 0
    mid = (start + end) // 2

    for i in inp:
        sum += (i // mid)
    
    if sum < k:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        

print(result)

