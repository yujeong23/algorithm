import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0

    # 행,열 범위 정해놓고 for문 반복하면서 더한 합 리스트에 넣기
    # 그 중에서 최대값 출력
    for i in range(N-M+1):
        for j in range(N-M+1):
            plus = 0
            for s in range(M):
                for l in range(M):
                    plus += arr[i+s][j+l]
            if max_sum < plus:
                max_sum = plus

    print('#{} {}'.format(tc, max_sum))