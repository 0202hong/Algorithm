import sys

inp = sys.stdin.readline().split()

sum = 0
for i in inp:
    sum += (int(i) ** 2)

print(sum % 10)