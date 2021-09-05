import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    line = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    stack = []

    for _ in range(E):
        s_line, e_line = map(int, input().split())
        line[s_line][e_line] = 1

    start, end = map(int, input().split())

    stack.append(start)
    visited[start] = 1
    result = 0

    while stack:                        # stack이 빌 때(처음부터 끝까지 돌았는데 끝 지점 도달 못 함)까지

        for j in range(1, V+1):
            if line[start][j] == 1 and visited[j] == 0:             # 돌면서 다음에 갈 곳 탐색
                    if j == end:                                    # 다음에 갈 곳이 도착 지점이면 끝
                        result = 1
                        stack = []
                        break
                    visited[j] = 1
                    stack.append(j)
                    start = j
                    break
        else:
            stack.pop()
            if stack:
                start = stack[-1]

    print('#{} {}'.format(tc, result))




