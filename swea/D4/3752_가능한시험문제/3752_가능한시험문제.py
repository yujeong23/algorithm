import sys
sys.stdin=open('sample_input.txt')

def cal(q, cnt):
    if cnt == q:
        temp = 0
        for idx in range(N):
            if check[idx]:
                temp += scores[idx]
        total.add(temp)
        return

    for i in range(N):
        if not check[i]:
            check[i] = 1
            cal(q, cnt+1)
            check[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    total = set()
    check = [0] * N
    for q in range(1, N+1):
        cal(q, 0)
    print(total)