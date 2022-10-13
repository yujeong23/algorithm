from itertools import combinations
from copy import deepcopy
# i가 i번쨰로 가는지 확인
def move():
    for m in range(N):
        now = m
        for num in range(H):
            if rails[num][now-1]:
                now -= 1
            elif rails[num][now]:
                now += 1
        if m != now:
            return 0
    else:
        return 1

def check(rows):
    flag = 0
    for row in rows:
        rails[row[0]][row[1]] = 1

    if move():
        flag = 1

    for row in rows:
        rails[row[0]][row[1]] = 0

    if flag:
        return 1
    else:
        return 0

N, M, H = map(int, input().split())
rails = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    rails[a-1][b-1] = 1

rows_lst = []
for i in range(N-1):
    for j in range(H):
        if not rails[j][i]:
            rows_lst.append([j, i])

for k in range(4):
    for rows in combinations(rows_lst, k):
        if check(rows):
            print(k)
            exit(0)
else:
    print(-1)

