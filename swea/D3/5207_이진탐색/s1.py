import sys
sys.stdin=open('input.txt')

def binarysearch(l, r):
    global check, cnt

    m = (l+r)//2

    if A[m] == b:                               # 정가운데 문자가 찾는 문자일 경우
        cnt += 1
        return

    if l == r:                                  # 끝까지 찾았는데 해당 문자가 없을 경우
        return

    elif A[m] > b:
        if check[-1] != '1':                    # 그 전에 오른쪽에서 넘어왔을 때만 재귀 (가지치기)
            check += '1'
            binarysearch(l, m-1)

    elif A[m] < b:
        if check[-1] != '0':                    # 그 전에 왼쪽에서 넘어왔을 때만 재귀 (가지치기)
            check += '0'
            binarysearch(m+1, r)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))  # 이진 탐색하기 위해서 정렬!!
    B = list(map(int, input().split()))
    cnt = 0

    for b in B:
        check = '2'                              # 양쪽 번갈아 찾는지 확인하기 위한 문자열
        binarysearch(0, N-1)

    print('#{} {}'. format(tc, cnt))

