import sys
from collections import deque
sys.stdin=open('sample_input.txt')

# 도로에는 나올 수 있는 값 중 가장 작은 값만 저장
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    road = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        road[s][e] = w
    node = [0] + [10000001] * N                 # 0번 도로는 이동 거리=0

    queue = deque([0])
    while queue:
        now = queue.popleft()
        for j in range(1, N+1):                                      # 조건 안 넣어주면 런타임 에러
            if road[now][j] and road[now][j] + node[now] < node[j]:  # 현재 도로와 연결되어있고 새롭게 저장될 값이 저장되어있는 값보다 작을 때
                node[j] = road[now][j] + node[now]                   # 더 작은 값으로 저장
                if j not in queue:                                   # queue에 이미 있다면 넣어주지 않기 (없어도 가능)
                    queue.append(j)


    print('#{} {}'.format(tc, node[N]))