N, M, K = map(int, input().split())
matrix = [[[] for _ in range(N)] for _ in range(N)]
balls = dict()
ans = 0
for idx in range(M):
    r, c, m, s, d = map(int, input().split())
    balls[idx] = [r-1, c-1, m, s, d]
    matrix[r-1][c-1].append(idx)

dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
while K:
    ans = 0
    for i in range(M):
        if balls[i]:
            tmp_r, tmp_c, tmp_m, tmp_s, tmp_d = balls[i]
            matrix[tmp_r][tmp_c].remove(i)
            nr = (balls[i][0] + (balls[i][3] * dr[balls[i][4]])) % N
            nc = (balls[i][1] + (balls[i][3] * dc[balls[i][4]])) % N
            balls[i][0], balls[i][1] = nr, nc
            matrix[nr][nc].append(i)

    for x in range(N):
        for y in range(N):
            if len(matrix[x][y]) > 1:
                l = len(matrix[x][y])
                total_m, total_s, odd, even = 0, 0, 0, 0
                for j in matrix[x][y]:
                    total_m += balls[j][2]
                    total_s += balls[j][3]
                    if balls[j][4] % 2:
                        odd += 1
                    else:
                        even += 1
                    balls[j] = 0
                total_m //= 5
                total_s //= l
                matrix[x][y] = []
                if total_m:
                    if odd == l or even == l:
                        dir = [0, 2, 4, 6]
                    else:
                        dir = [1, 3, 5, 7]
                    for num in range(4):
                        balls[M+num] = [x, y, total_m, total_s, dir[num]]
                        matrix[x][y].append(M+num)
                    ans += total_m * 4
                    M += 4
            elif len(matrix[x][y]) == 1:
                ans += balls[matrix[x][y][0]][2]
    K -= 1

print(ans)