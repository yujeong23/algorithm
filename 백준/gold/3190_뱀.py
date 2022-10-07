from collections import deque

N = int(input())
K = int(input())
dummy = [[0] * N for _ in range(N)]
dummy[0][0] = 2
for _ in range(K):
    r, c = map(int, input().split())
    dummy[r-1][c-1] = 1
L = int(input())
dir = [0] * N * N
for _ in range(L):
    X, C = map(str, input().split())
    dir[int(X)] = C

deq = deque([[0, 0]])
cnt = 1
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y, k = 0, 0, 0

while True:
    nx, ny = x+dx[k], y+dy[k]
    if nx in range(N) and ny in range(N):
        if dummy[nx][ny] == 2:
            break
        elif dummy[nx][ny] == 1:
            dummy[nx][ny] = 2
        else:
            tx, ty = deq.popleft()
            dummy[tx][ty] = 0
            dummy[nx][ny] = 2
        deq.append([nx, ny])
    else:
        break
    if dir[cnt] == 'D':
        k = (k+1) % 4
    elif dir[cnt] == 'L':
        if k:
            k -= 1
        else:
            k = 3
    x, y = nx, ny
    cnt += 1

print(cnt)