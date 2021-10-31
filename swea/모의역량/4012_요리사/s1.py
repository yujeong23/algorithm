import sys
sys.stdin=open('input.txt')

def cal(A, B):
    global result
    A_sum = 0
    B_sum = 0
    for m in range(N//2 - 1):
        for n in range(m+1, N//2):
            A_sum += food[A[m]][A[n]] + food[A[n]][A[m]]
            B_sum += food[B[m]][B[n]] + food[B[n]][B[m]]
    if abs(A_sum - B_sum) < result:
        result = abs(A_sum-B_sum)

def comb(idx, A):
    if len(A) == N // 2:                # A에 들어갈 재료 다 뽑았다면
        B = []                          # A 리스트에 안 들어간 재료 B 조합 만들기
        for j in lst:
            if j not in A:
                B.append(j)
        cal(A, B)                       # 시너지 계산
        return

    for i in range(idx, N):           # A 음식에 들어갈 재료 조합 만들기
        comb(i+1, A+[lst[i]])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]
    result = 200000
    lst = []
    for i in range(N):
        lst.append(i)
    comb(0, [])

    print('#{} {}'.format(tc, result))


