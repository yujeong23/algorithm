import sys
sys.stdin = open('input.txt')

def charge(now, cnt):
    global minV

    if cnt > minV:                    # 가지치기
        return

    if now >= N:                      # 현재 위치가 도착지점을 넘어갔을 때
        minV = cnt-1                  # 마지막 도착지에서는 충전을 안 시키므로 cnt 1 빼주기
        return

    for i in range(1, stop[now]+1):   # 충전시켰을 때 갈 수 있는 정류장 모두 가보기
        charge(now+i, cnt+1)          # 도착하면 cnt 바로 증가



T = int(input())
for tc in range(1, T+1):
    stop = list(map(int, input().split()))
    N = stop[0]
    minV = N
    charge(1, 0)                     # 현재 정류장, 충전 횟수
    print('#{} {}'.format(tc, minV))