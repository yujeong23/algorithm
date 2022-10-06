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
    dist = 0
    for s1, s2 in lst:
        for d1, d2 in house:
            dist += abs(s1-d1) + abs(s2-d2)
    
