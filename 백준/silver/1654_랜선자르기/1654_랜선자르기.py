def binary_search(s, e):
    global result

    mid = (s+e) // 2
    cnt = 0
    for lan in lans:
        cnt += lan // mid

    if cnt >= N:
        result.append(mid)

    if s <= e:
        if cnt < N:
            binary_search(0, mid+1)
        else:
            binary_search(mid, e)


K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]
result = []

if min(lans) == max(lans):
    print(lans[-1])
else:
    binary_search(0, max(lans))
    print(max(result))