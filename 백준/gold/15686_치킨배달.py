from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
ans = 987654321
for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            house.append([r, c])
        elif city[r][c] == 2:
            chicken.append([r, c])

for lst in combinations(chicken, M):
    total = 0
    for d1, d2 in house:
        dist = N*N
        for s1, s2 in lst:
            dist = min(dist, abs(s1-d1) + abs(s2-d2))
        total += dist
    ans = min(ans, total)

print(ans)
