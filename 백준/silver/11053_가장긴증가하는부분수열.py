# 앞의 숫자들 중에서 현재 숫자보다 작은 수 모두 확인
# 그 중에서 제일 큰 값이 저장된 수 + 1
N = int(input())
A = list(map(int, input().split()))
dp = [1] * N
for i in range(N):
    maxv = 0
    for j in range(i):
        if A[j] < A[i] and dp[j] > maxv:
            maxv = dp[j]
    dp[i] = maxv + 1

print(max(dp))