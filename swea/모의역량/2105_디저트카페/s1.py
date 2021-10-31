import sys
sys.stdin=open('input.txt')

def tour(r, c, line):
    visited = set()
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]

    for i in range(4):
        for _ in range(line[i]):
            r, c = r + dr[i], c + dc[i]
            if dessert[r][c] in visited:    # 먹었던 디저트가 또 나온 경우 바로 return
                return 0
            visited.add(dessert[r][c])
    return 1

def check(w, h):
    for r in range(0, N - w - h):           # 시작점이 될 수 있는 (r, c) 모두 확인 (r+h+w < N)
        for c in range(h, N - w):           # 0 <= c-h, c+w < N
            if tour(r, c, [w, h, w, h]):
                return 1
    return 0                                # 가능한 시작지점 모두 확인했는데도 만족하는 경로가 없는 경우

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]

    ans = -1                        # 사각형 변의 길이 정하기
    for l in range(N-1, 1, -1):     # w(가로) + h(세로) = l, 길이가 긴 것부터 확인
        for w in range(1, l):
            if check(w, l-w):       # h = l-w
                ans = l * 2
                break
        if ans != -1:
            break

    print('#{} {}'.format(tc, ans))