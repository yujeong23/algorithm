import sys
from collections import deque
sys.stdin=open('sample_input.txt')

def move(i, j, fuel):
    global visited

    di = [0, +1, -1, 0]
    dj = [+1, 0, 0, -1]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N:                             # 다음 이동 위치가 범위 안에 있다면
            minus = height[ni][nj] - height[i][j]

            if minus > 0 and fuel+minus+1 < visited[ni][nj]:        # 다음 위치가 더 높을 때, 저장될 값이 현재값보다 더 작을 떄만 이동
                queue.append([ni, nj])
                visited[ni][nj] = fuel+minus+1

            elif minus <= 0 and fuel+1 < visited[ni][nj]:           # 다음 위치가 더 낮을 때
                queue.append([ni, nj])
                visited[ni][nj] = fuel+1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]
    visited = [[100000*N*N] * N for _ in range(N)]                  # visited에 비용 최소 비용 누적

    visited[0][0] = 0                                               # (0, 0) 부터 시작
    queue = deque([[0, 0]])

    while queue:
        i, j = queue.popleft()
        move(i, j, visited[i][j])

    print('#{} {}'.format(tc, visited[-1][-1]))