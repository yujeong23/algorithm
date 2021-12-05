from collections import deque

def dfs(start):                        # 스택 이용
    stack = [start]
    result = []
    while stack:
        num = stack.pop()
        if num not in result:
            result.append(num)
            temp = sorted(lst[num], reverse=True)
            for n in temp:
                stack.append(n)
    return result

def bfs(start):                         # 큐 이용
    deq = deque([start])
    result = []
    while deq:
        num = deq.popleft()
        if num not in result:
            result.append(num)
            temp = sorted(lst[num])     # 작은 숫자부터 이동하도록
            for n in temp:
                deq.append(n)
    return result

N, M, V = map(int, input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

print(*dfs(V))
print(*bfs(V))