import sys
sys.stdin = open('input.txt')

def game(N, arr):
    result1 = []
    result2 = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                result1 += arr[i][j]
            if arr[j][i] == 'o':
                result2 += arr[j][i]
        if len(result1) >= 5 or len(result2) >= 5:
            return ('yes')
        result1, result2 = [], []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                i -= 1
                j -= 1




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [str(input()) for _ in range(N)]
    print('#{} {}'.format(tc, game(N, arr)))