import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = []
    B = []
    # _번쨰 버스가 다니는 노선이 Ai이상 Bi이하
    # Ai, Bi를 A,B 리스트에 저장
    for _ in range(N):
        a, b = map(int,input().split())
        A.append(a)
        B.append(b)
    P = int(input())
    # 구하려고 하는 버스 정류장을 리스트에 저장
    bus_stop = []
    for p in range(P):
        bus_stop.append(int(input()))

    cnt = [0]*5001
    for j in range(N):
        for i in range(A[j], B[j]+1):
            cnt[i] += 1

    result = []
    for bus in bus_stop:
        result.append(cnt[bus])

    print('#{}'.format(tc), *result)