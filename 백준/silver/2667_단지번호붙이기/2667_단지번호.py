# bfs => deque이용
from collections import deque
def bfs(i, j):
    deq = deque([(i, j)])
    num = 1

    while deq:
        i, j = deq.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni in range(N) and nj in range(N) and matrix[ni][nj]:
                deq.append((ni, nj))
                matrix[ni][nj] = 0
                num += 1

    return num

# dfs => 재귀 이용
def dfs(i, j):
    global cnt

    if i in range(N) and j in range(N) and matrix[i][j]:
        cnt += 1
        matrix[i][j] = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            dfs(ni, nj)


N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input())))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

result = []

for i in range(N):
    for j in range(N):
        if matrix[i][j]:
            # matrix[i][j] = 0
            # result.append(bfs(i, j))
            cnt = 0
            dfs(i, j)
            result.append(cnt)


result.sort()
print(len(result))
for num in result:
    print(num)