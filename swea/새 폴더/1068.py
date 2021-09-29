import sys
sys.stdin = open('input.txt')

def kill_node(k):
    if k in leaf:
        leaf.remove(k)
        if len(node_tree[tree[k]]) == 1:
            leaf.append(tree[k])
            k = tree[tree[k]]
            if kill == node_tree[tree[k]]:
                return

            elif k == -1:
                leaf.pop(-1)
                return
    if len(node_tree[k]) == 0:
        return
    else:
        for i in range(len(node_tree[k])):
            kill_node(node_tree[k][i])


N = int(input())
tree = list(map(int, sys.stdin.readline().split()))
kill = int(input())

node_tree = [[] for _ in range(N)]
for i in range(N):
    if tree[i] == -1:
        continue
    node_tree[tree[i]].append(i)
print(node_tree)
leaf = []
for x in range(N):
    if not node_tree[x]:
        leaf.append(x)
print(leaf)
kill_node(kill)
print(len(leaf))