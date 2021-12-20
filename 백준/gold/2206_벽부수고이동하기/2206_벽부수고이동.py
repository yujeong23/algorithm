'''
방문체크는 왔던 곳 한 번 더 안 오려고!!
벽을 한 번도 안 부셨을 때, 벽을 이미 부수고 지나왔을 때
나눠서 방문 체크 두 번 하기
벽을 한 번 부수고 왔을 때는 갈 수 없는 길이어도(-1 return)
한 번도 부수지 않았을 때는 가능한 길이 될 수 있음
'''
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

def bfs(N, M):
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]       # 3차원 배열 (벽을 부시지 않았을 때, 부셨을 때 방문 체크)
    deq = deque([(0, 0, 1, 0)])
    visited[0][0][0] = 1

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while deq:
        i, j, cnt, broken = deq.popleft()

        if i == N-1 and j == M-1:
            return cnt

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni in range(N) and nj in range(M):
                if graph[ni][nj] == 0 and not visited[broken][ni][nj]:
                    deq.append((ni, nj, cnt+1, broken))
                    visited[broken][ni][nj] = 1

                elif graph[ni][nj] == 1 and not visited[1][ni][nj]:    # 벽이면 한 번 부수기
                    if broken == 0:
                        deq.append((ni, nj, cnt+1, 1))
                        visited[1][ni][nj] = 1

    return -1

print(bfs(N, M))