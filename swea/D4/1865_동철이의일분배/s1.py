import sys
sys.stdin = open('input.txt')

def select(p, now):
    global success

    if now < success:                       # 현재 계산된 값이 최대 성공률보다 작다면 가지치기
        return

    if sum(people) == N:                    # 직원이 모두 배정되었다면 성공률 저장
        success = now
        return

    for i in range(N):
        if not people[i] and work[p][i]:    # 아직 배정된 직원이 아니고, 성공률이 0이 아니라면 성공률 계싼하기
            people[i] = 1
            percent = work[p][i]
            select(p+1, now*percent)
            people[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work = [list(map(lambda x: float(x)/100, input().split())) for _ in range(N)]   # 100으로 나눈 값으로 입력 저장
    people = [0] * N                # 배정된 직원 체크
    success = 0                     # 성공률 계산
    select(0, 1)

    print('#{} {:.6f}'.format(tc, success*100))