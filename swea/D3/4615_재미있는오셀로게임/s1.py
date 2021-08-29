import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int,input())
    board = [[0] * N for _ in range(N)]
    board[N/2-1][N/2], board[N/2][N/2-1] = 1, 1
    board[N/2-1][N/2-1], board[N/2][N/2] = 2, 2
    di = [-2, +2, 0, 0] # 상하좌우
    dj = [0, 0, -2, +2]
    for _ in range(M):
        j, i, color = map(int,input())
        board[i-1][j-1] = color
        for k in range(4):
            if board[i-1+di[k]][j-1+dj[k]] == color:
                board[i-1+(di[k]/2)][j-1+(dj[k]/2)]
