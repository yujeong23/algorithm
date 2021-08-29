import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    flag = [list(input()) for _ in range(N)]
    cnt = 0

    for j in range(M):                  # 맨 첫째줄, 마지막 줄 각각 W, R로 고정
        if flag[0][j] != 'W':
            flag[0][j] = 'W'
            cnt += 1
        if flag[N-1][j] != 'R':
            flag[N - 1][j] = 'R'
            cnt += 1

    min_cnt = (N-2) * M
    for i in range(N-3, -1, -1):             # W줄의 최대 개수
        for j in range(1, N-1-i):            # B줄의 최대 개수
            new_cnt = 0
            for x in range(1, 1+i):
                for y in range(M):
                    if flag[x][y] != 'W':
                        new_cnt += 1
            for x in range(1+i, i+j+1):
                for y in range(M):
                    if flag[x][y] != 'B':
                        new_cnt += 1
            for x in range(i+j+1, N):
                for y in range(M):
                    if flag[x][y] != 'R':
                        new_cnt += 1
            if min_cnt > new_cnt:
                min_cnt = new_cnt

    result = cnt + min_cnt

    print('#{} {}'.format(tc, result))