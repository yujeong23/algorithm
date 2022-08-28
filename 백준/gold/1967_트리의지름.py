import sys
sys.setrecursionlimit(10 ** 9)

def dfs(node, num):
    for n, v in tree[node]:
        if visited[n] == -1:
            visited[n] = num+v
            dfs(n, num+v)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    nodes = list(map(int, input().split()))
    tree[nodes[0]].append([nodes[1], nodes[2]])
    tree[nodes[1]].append([nodes[0], nodes[2]])

visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)
start = visited.index(max(visited))

visited = [-1] * (n+1)
visited[start] = 0
dfs(start, 0)
print(max(visited))