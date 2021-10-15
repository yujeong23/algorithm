import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        alpha, num = map(str,input().split())
        lst += alpha * int(num)
    print('#{}'.format(tc))
    if (len(lst)//10):
        for _ in range(len(lst) // 10):
            new_lst = []
            for _ in range(10):
                new_lst += lst[0]
                lst.remove(lst[0])
            print(''.join(new_lst))
    print(''.join(lst))



