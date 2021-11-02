from collections import deque
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    visited[-1][-1] = 1
    queue = deque([(n-1, m-1, 1)])
    result = -1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y, cnt = queue.popleft()
        if x == 0 and y == 0:
            result = cnt
            break

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if nx in range(n) and ny in range(m):
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx, ny, cnt+1))
                    visited[nx][ny] = 1

    return result

print(solution(maps))

# 효율성 x
# 최단거리니까 그냥 bfs로 한 번에 구하면 된다!!
# def solution(maps):
#     n, m = len(maps), len(maps[0])
#     queue = deque([(n-1, m-1, 1)])
#     result = 0
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     while queue:
#         x, y, cnt = queue.popleft()
#         maps[x][y] = cnt
#         if x == 0 and y == 0:
#             return cnt
#
#         for k in range(4):
#             nx, ny = x + dx[k], y + dy[k]
#
#             if nx in range(n) and ny in range(m):
#                 if maps[nx][ny] == 1 or maps[nx][ny] > cnt + 1:
#                     queue.append((nx, ny, cnt+1))
#
#     return -1