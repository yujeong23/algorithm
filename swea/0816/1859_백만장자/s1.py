import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int,input().split()))
#
#     profit = 0
#     while len(lst) != 0:
#         max_idx = lst.index(max(lst))
#         profit += (lst[max_idx] * max_idx) - sum(lst[:max_idx])
#         lst = lst[max_idx + 1:N]
#     print('#{} {}'.format(tc, profit))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    maxV = lst[-1]
    profit = 0
    for i in range(len(lst) - 1, -1, -1):
        if maxV > lst[i]:
            profit += maxV - lst[i]
        else:
            maxV = lst[i]
    print("#{} {}".format(tc, profit))