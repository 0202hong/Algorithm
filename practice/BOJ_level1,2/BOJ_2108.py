N = int(input())
dic = {}

for _ in range(N):
    inp = int(input())
    if inp in dic.keys():
        dic[inp] += 1
    else:
        dic[inp] = 1

sum = 0
for i, j in dic.items():
    sum += i * j

print(f'{round(sum / N)}') #산술 평균

arr = [[i for _ in range(j)] for i, j in dic.items()]

print(arr)