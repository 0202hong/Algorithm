import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
card = [int(i) for i in sys.stdin.readline().rstrip().split()]

card.sort()

result = 0
for i in range(len(card) - 2):
    for j in range(i + 1, len(card) - 1):
        for k in range(j + 1, len(card)):
            if card[i] + card[j] + card[k] <= M:
                if (M - (card[i] + card[j] + card[k])) < (M - result):
                    result = card[i] + card[j] + card[k]

print(result)