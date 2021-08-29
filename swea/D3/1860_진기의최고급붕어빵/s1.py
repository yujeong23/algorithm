import sys
sys.stdin = open('input.txt')

def sell(M, K, t):
    stack = []

    if 0 in t:                      # 0초에 오는 손님도 있음 -> 무조건 붕어빵 못 받음
        return 'Impossible'

    for i in range(1, max(t)+1):
        if (i % M) == 0:
            stack += [1] * K         # list에 한 번에 K개씩 쌓이게 하려면 append 이용하면 안 됨 주의
        if i in t:
            while i in t:
                if stack:
                    stack.pop(0)
                    idx = t.index(i)
                    t.pop(idx)
                else:
                    return 'Impossible'
    return 'Possible'

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    t = list(map(int, input().split()))
    print('#{} {}'.format(tc, sell(M, K, t)))

