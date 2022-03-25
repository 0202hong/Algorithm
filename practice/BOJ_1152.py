import sys

input = sys.stdin.readline().rstrip()

dic = {}
for i in input:
    i = i.upper()
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

# print(input)
# print(dic)

dic_tolist = [(i, j) for i, j in dic.items()]
dic_tolist.sort(key = lambda x : x[1], reverse = True)
if len(input) == 1: print(dic_tolist[0][0])
elif dic_tolist[0][1] == dic_tolist[1][1]:
    print('?')
else:
    print(dic_tolist[0][0])