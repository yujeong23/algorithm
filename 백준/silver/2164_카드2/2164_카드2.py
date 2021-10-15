import sys
from collections import deque
N = int(sys.stdin.readline())

card_q = deque()
for i in range(1, N+1):
    card_q.append(i)

while len(card_q) > 1:
    card_q.popleft()
    first = card_q.popleft()
    card_q.append(first)


print(card_q[0])