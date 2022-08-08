def cal(now):
    if now == n-1:
        return

n, m = map(int, input().split())
names = list(int(input()) for _ in range(n))
cal(0)