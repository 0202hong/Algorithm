import sys

inp = []
for _ in range(9):
    inp.append(int(sys.stdin.readline()))

max_idx = 0
max_value = 0
for i, j in enumerate(inp):
    if max_value < j:
        max_value = j
        max_idx = i

print(f'{max_value}\n{max_idx + 1}')