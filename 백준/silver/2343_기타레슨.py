# 블루레이 하나의 크기를 이분탐색
# 블루레이 크기를 정해두고, 블루레이에 몇 개의 강의가 들어갈 수 있는지 확인(cnt)
N, M = map(int, input().split())
time = list(map(int, input().split()))
ans = 10000 * N
# 블루레이 갯수 확인
def check(num):
    global ans

    cnt = 1
    temp = num
    for t in time:
        if temp >= t:
            temp -= t
        else:
            cnt += 1
            temp = num
            temp -= t

    return cnt

s = max(time)
e = sum(time)
maxv = max(time)

while s <= e:
    mid = (s+e) // 2
    cnt = check(mid)
    # 블루레이 갯수가 M보다 많음 -> 블루레이 하나의 크기가 작다
    if cnt > M:
        s = mid+1
    else:
        e = mid-1
        # 블루레이 갯수가 M보다 적음 -> M개 맞출 수 있으므로 cnt == M일 필요 x
        ans = min(ans, mid)

print(ans)