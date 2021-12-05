import sys
sys.stdin=open('input.txt')

N, D = map(int, input().split())
distance = [i for i in range(D+1)]
lst = []

for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.sort()

for s, e, l in lst:
    if e - s > l and e in range(D + 1):
        distance[e] = min(distance[e], distance[s] + l)
        for i in range(1, D+1):
            distance[i] = min(distance[i], distance[i-1]+1)

print(distance[-1])

