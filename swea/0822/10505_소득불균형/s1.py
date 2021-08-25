import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    sum_lst = sum(lst)
    avg = sum(lst) / len(lst)
    cnt = 0
    for num in lst:
        if num <= avg:
            cnt += 1

    print('#{} {}'.format(tc, cnt))