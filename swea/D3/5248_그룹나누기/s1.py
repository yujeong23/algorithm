import sys
sys.stdin=open('sample_input.txt')

def check(p):
    stack = [p]
    while stack:
        i = stack.pop()
        for j in range(1, N+1):
            if people[i][j] == 1:
                stack.append(j)
                group[j] = cnt                         # 그룹으로 묶어주기
                people[i][j] = people[j][i]= 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    people = [[0] * (N+1) for _ in range(N+1)]
    for i in range(M):
        a, b = lst[2 * i], lst[2 * i + 1]
        people[a][b] = people[b][a] = 1

    group = [0] * (N + 1)               # 사람마다 그룹 설정
    cnt = 0
    for p in range(1, N + 1):           # 그룹이 없는 사람들(값이 0인 사람들)만 그룹 찾기
        if not group[p]:
            cnt += 1
            group[p] = cnt              # 해당 그룹 번호로 group 설정
            check(p)

    print('#{} {}'.format(tc, cnt))