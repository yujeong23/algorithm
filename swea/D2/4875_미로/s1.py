import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    stack = []
    result = 0
    x, y = 0, 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x = i
                y = j
                break

    visited[x][y] = 1
    stack.append([x, y])
    # 상하좌우
    dx = [0, 0, -1, +1]
    dy = [-1, +1, 0, 0]

    while stack:
        x, y = stack.pop()
        visited[x][y] = 1

        if maze[x][y] == 3:
            result = 1
            stack = []
            break

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if (-1 < nx < N) and (-1 < ny < N) and (maze[nx][ny] != 1) and (visited[nx][ny] == 0):
                stack.append([nx, ny])


    print('#{} {}'.format(tc, result))