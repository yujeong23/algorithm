import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 배열 상하좌우에 0을 한 줄씩 넣어주기
    puzzle = [[0] * (N+2)] + [[0] + list(map(int,input().split())) + [0] for _ in range(N)] + [[0] * (N+2)]
    # 찾을 단어크기 양 옆에 0을 넣어주기
    word = [0] + [1]*K +[0]
    # 행렬을 바꾼 배열 생성
    puzzle_col = [[0] * (N+2) for _ in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            puzzle_col[i][j] = puzzle[j][i]

    cnt = 0

    #puzzle, puzzle_col 배열을 돌면서 word와 같은 부분을 찾으면 cnt하나씩 추가
    for i in range(N+2):
        for j in range(N+2):
            if puzzle[i][j:j+K+2] == word:
                cnt += 1
            if puzzle_col[i][j:j + K + 2] == word:
                cnt += 1
    print ('#{} {}'.format(tc, cnt))

