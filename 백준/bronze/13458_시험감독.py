N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = N
for place in A:
    if place >= B:
        student = place - B
        ans += student // C
        if student % C:
            ans += 1
print(ans)