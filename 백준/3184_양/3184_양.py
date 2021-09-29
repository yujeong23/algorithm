import sys
sys.stdin=open('input.txt')

def bfs(x, y):
    global w, s, visited
    check = [[x,y]]
    visited[x][y] = 1
    while check:
        x, y = check.pop()


        if ground[x][y] == 'v':
            w += 1

        elif ground[x][y] == 'o':
            s += 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < R and 0 <= ny < C and ground[nx][ny] != '#' and not visited[nx][ny]:
                check.append([nx, ny])
                visited[nx][ny] = 1



R, C = map(int, input().split())

ground = []
for _ in range(R):
    ground.append(list(input()))

visited = [[0] * C for _ in range(R)]           # 방문 체크
     # 우 좌 상 하
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


wolf = 0
sheep = 0
for x in range(R):
    for y in range(C):
        if not visited[x][y] and ground[x][y] != '#':
            w, s = 0, 0
            bfs(x, y)
            if w >= s:
                wolf += w
            elif w < s:
                sheep += s

print(sheep, wolf)