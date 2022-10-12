R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
machine = []
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
while T:
    # 먼지 확산
    tmp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if len(machine) < 2 and room[i][j] == -1:
                machine.append([i, j])
            elif room[i][j] > 0:
                cnt = 0
                dust = room[i][j] // 5
                for k in range(4):
                    ni, nj = i+di[k], j+dj[k]
                    if ni in range(R) and nj in range(C) and [ni, nj] not in machine:
                        cnt += 1
                        tmp[ni][nj] += dust
                room[i][j] -= dust * cnt
    for x in range(R):
        for y in range(C):
            room[x][y] += tmp[x][y]
    # 공기청정기
    ur, uc = machine[0][0], machine[0][1]
    dr, dc = machine[1][0], machine[1][1]
    room[ur][uc], room[dr][dc] = 0, 0
    up_d, down_d = 0, 0
    for m in range(1, C):
        temp_u = room[ur][m]
        room[ur][m] = up_d
        up_d = temp_u

        temp_d = room[dr][m]
        room[dr][m] = down_d
        down_d = temp_d

    for un in range(ur-1, -1, -1):
        temp_u = room[un][C-1]
        room[un][C-1] = up_d
        up_d = temp_u
    for dn in range(dr+1, R):
        temp_d = room[dn][C-1]
        room[dn][C-1] = down_d
        down_d = temp_d

    for m in range(C-2, -1, -1):
        temp_u = room[0][m]
        room[0][m] = up_d
        up_d = temp_u

        temp_d = room[R-1][m]
        room[R-1][m] = down_d
        down_d = temp_d

    for un in range(1, ur):
        temp_u = room[un][0]
        room[un][0] = up_d
        up_d = temp_u
    for dn in range(R-2, dr, -1):
        temp_d = room[dn][0]
        room[dn][0] = down_d
        down_d = temp_d

    T -= 1

print(sum(sum(room[i]) for i in range(R)))