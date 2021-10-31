import sys
from collections import deque
sys.stdin=open('input.txt')
# 제거 함수
def bomb(i, j, map):
    num = map[i][j]
    queue = deque([(i, j, num)])
        # 상 하 좌 우
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]

    while queue:
        x, y, num = queue.popleft()
        map[x][y] = 0
        for n in range(1, num):
            for k in range(4):
                nx = x + n*dx[k]
                ny = y + n*dy[k]
                if 0<= nx < H and 0<= ny < W and map[nx][ny] != 0:
                    queue.append((nx, ny, map[nx][ny]))
                    map[nx][ny] = 0

    for col in range(W):
        idx = H -1
        for row in range(H-1, -1, -1):
                if not map[row][col]:
                    continue
                map[idx][col], map[row][col] = map[row][col], map[idx][col]
                idx -= 1

    return map

def find(cnt, map):
    global mincnt

    result = 0
    for x in range(H):
        for y in range(W):
            if map[x][y]:
                result += 1
    if result == 0:
        mincnt = 0
        return

    if cnt == 0:
        if result < mincnt:
            mincnt = result
        return


    for j in range(W):                      # 맨 위의 폭탄 떨어질 위치 찾기
        for i in range(H):
            if map[i][j] != 0:
                temp_brick = [data[:] for data in map]
                new_map = bomb(i, j, temp_brick)
                find(cnt-1, new_map)
                break



T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(H)]

    mincnt = W * H
    find(N, brick)

    print('#{} {}'.format(tc, mincnt))
