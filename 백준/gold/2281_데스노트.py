# 모든 줄에서 해당 단어를 처음 시작했을 때 나머지 칸 개수로 dp
n, m = map(int, input().split())
notes = [int(input()) for _ in range(n)]
dp = [float('inf')] * n
dp[-1] = 0
for i in range(n-2, -1, -1):
    dp[i] = (m - notes[i]) ** 2 + dp[i+1]

    name = notes[i]
    for j in range(i+1, n):
        name += notes[j] + 1
        if name > m:
            break

        if j == n-1:
            dp[i] = 0
            continue

        num = (m - name) ** 2
        if j+1 in range(n):
            num += dp[j+1]

        dp[i] = min(dp[i], num)

print(dp[0])