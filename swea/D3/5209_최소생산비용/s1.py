import sys
sys.stdin = open('input.txt')

def cal(i, result):
    global minV, checked

    if result > minV:                 # 중간까지 더한 값이 이미 최솟값보다 크다면 가지치기
        return

    if len(checked) == N:             # 공장이 모두 정해졌다면 결과와 현재 최솟값 비교
        minV = result
        return

    for j in range(N):                  # 완전 탐색
        if j not in checked:
            checked.append(j)           # 방문했으므로 체크
            cal(i+1, result+arr[i][j])
            checked.pop()               # 방문체크 지우기


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = float('inf')
    checked = []                        # 방문체크
    cal(0, 0)
    print('#{} {}'.format(tc, minV))