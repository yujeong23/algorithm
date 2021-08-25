import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    farm = [list(map(int,input())) for _ in range(N)]

    sum = 0                                      # 가운데 행을 기점으로 윗부분
    mid = N // 2
    for i in range(mid+1):                      # 가운데 열을 기준으로 양쪽에 위치한 수를 더함
        for k in range(i+1):
            sum += farm[i][mid-k]
            farm[i][mid-k] = 0
            sum += farm[i][mid+k]

    for i in range(N-1, mid, -1):                # 가운데 행을 기점으로 아랫부분
        for k in range(N-i):
            sum += farm[i][mid-k]
            farm[i][mid-k] = 0
            sum += farm[i][mid+k]

    print ('#{} {}'.format(tc, sum))