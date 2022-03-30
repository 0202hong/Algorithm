N = int(input())

arr = [int(i) for i in range(1, N + 1)]
arr.sort(reverse = True)
print(*arr, sep = '\n')