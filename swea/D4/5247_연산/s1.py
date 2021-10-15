import sys
from collections import deque
sys.stdin=open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = [0] * 1000001                              # index 이용
    mincnt = abs(M - N)                                 # 초기값에서 +1 계속 해줬을 때를 최솟값으로 설정
    queue = deque([[N, 0]])                             # 초기값부터 연산 하나씩 해주면서 M될 때까지 확인

    while queue:
        ans, cnt = queue.popleft()
        if ans == M:
            mincnt = cnt
            break

        op_lst = [ans + 1, ans - 1, ans * 2, ans - 10]
        for op in op_lst:
            if 0 < op < 1000001 and not result[op]:     # and 사용할 때 위치 중요!!(순서가 바뀌면 op값이 범위값을 넘어가면 인덱스 에러)
                result[op] = cnt + 1                    # 인덱스에 저장
                queue.append([op, cnt+1])

    print('#{} {}'.format(tc, mincnt))