from collections import deque

N = int(input())

q = deque([int(i) for i in range(1, N + 1)])

if N > 1:
    q.popleft()
    while len(q) != 1:
        q.append(q.popleft())
        if len(q) > 1:
            q.popleft()

    print(q.pop())
else: print(1)