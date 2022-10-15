from itertools import combinations
from collections import deque

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
viruses = []
zero = 0
for x in range(N):
    for y in range(N):
        if lab[x][y] == 2:
            viruses.append([x, y])
        elif lab[x][y] == 0:
            zero += 1
if not zero:
    print(0)
    exit(0)
combs = combinations(viruses, M)
inf = float('inf')
ans = inf
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
for comb in combs:
    visited = [[0] * N for _ in range(N)]
    deq = deque([])
    for c in comb:
        lst = c + [1]
        deq.append(lst)
        visited[lst[0]][lst[1]] = 1

    cnt = 0
    while deq:
        r, c, time = deq.popleft()

        for k in range(4):
            nr, nc = r+dr[k], c+dc[k]
            if nr in range(N) and nc in range(N) and not visited[nr][nc]:
                if lab[nr][nc] == 0:
                    visited[nr][nc] = 1
                    deq.append([nr, nc, time+1])
                    cnt += 1
                elif lab[nr][nc] == 2:
                    visited[nr][nc] = 1
                    deq.append([nr, nc, time+1])

        if cnt == zero:
            ans = min(ans, time)

print(ans if ans != inf else -1)