N = int(input())
time = [0] * (N+1)
pay = [0] * (N+1)
result = [0] * (N+2)
ans = 0
for i in range(N):
    T, P = map(int, input().split())
    time[i+1] = T
    pay[i+1] = P

for j in range(1, N+1):

    if j + time[j] in range(N+2):
        result[j + time[j]] = max(result[j + time[j]], result[j]+pay[j])
        ans = max(ans, result[j + time[j]])
print(result)
print(max(result))