import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    score_lst = []
    lst_new = []
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for _ in range(N):
        a, b, c = map(int, input().split())
        score = (0.35*a) + (0.45*b) + (0.2*c)
        score_lst.append(score)
    score_k = score_lst[K-1]
    # 몇 등인지 확인하기 위해 본인 점수보다 큰 점수가 있으면 cnt를 하나씩 늘려줌
    cnt = 1
    for score in score_lst:
        if score > score_k:
            cnt += 1
    # 학생 점수 순위가 경계에 걸릴 때 인덱스가 다르므로 범위를 나누어줘야한다.
    if cnt % (N/10):
        result = grade[int(cnt // (N/10))]
    else:
        result = grade[int(cnt // (N / 10))-1]
    print('#{} {}'.format(tc, result))



