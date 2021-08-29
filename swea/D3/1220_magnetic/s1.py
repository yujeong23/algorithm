import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for j in range(N):
        stack = []
        for i in range(N):
            if arr[i][j] == 1:
                stack.append(arr[i][j])
            elif arr[i][j] == 2 and stack:
                stack = []                    # 처음에 stack.pop() 쓰려고 했는데 빨강 두 개, 파랑 두 개가 연속으로 나올 경우도
                cnt += 1                      # 교착 상태 한 번이라고 치기 때문에 그냥 stack을 비워줌

    print('#{} {}'.format(tc, cnt))
