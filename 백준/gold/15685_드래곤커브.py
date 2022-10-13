def move(x, y, d, g):
    global dragons

    dragons[x][y] = 1
    nx, ny = x + dx[d], y + dy[d]
    dragons[nx][ny] = 1
    x, y = nx, ny
    visited = [d]

    for _ in range(g):
        l = len(visited)
        for idx in range(l-1, -1, -1):
            dir = (visited[idx] + 1) % 4
            x, y = x+dx[dir], y+dy[dir]
            dragons[x][y] = 1
            visited.append(dir)


N = int(input())
dragons = [[0] * 101 for _ in range(101)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
for _ in range(N):
    y, x, d, g = map(int, input().split())
    move(x, y, d, g)

ans = 0
for i in range(100):
    for j in range(100):
       if dragons[i][j] and dragons[i+1][j] and dragons[i][j+1] and dragons[i+1][j+1]:
           ans += 1

print(ans)
