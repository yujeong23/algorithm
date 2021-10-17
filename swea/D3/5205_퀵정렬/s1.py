import sys
sys.stdin=open('input.txt')

def partition(A, l, r):
    p = A[l]                        # 시작 인덱스를 피봇으로 설정
    i = l+1                         # 피봇 다음부터 정렬
    j = r
    while i <= j:
        while i <= j and A[i] <= p:  # i가 j를 넘어가지 않고, 피봇보다 작을 때까지 뒤로 보내기
            i += 1
        while i <= j and A[j] >= p:  # j가 i보다 작아지지 않고, 피봇보다 클 때까지 앞으로 보내기
            j -= 1
        if i <= j:                   # i, j가 만나기 전이라면 위치 바꾸면서 정렬
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]         # 리스트 모두 확인했다면 피봇값 중간에 껴주기
    return j

def quick_sort(A, l, r):

    if l < r:

        k = partition(A, l, r)      # 중간에 껴준 피봇 기준으로 왼, 오 다시 정렬

        quick_sort(A, l, k-1) 
        quick_sort(A, k+1, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    quick_sort(A, 0, N-1)                   # 정렬할 리스트, 시작 인덱스, 끝 인덱스
    print('#{}'.format(tc), A[N//2])