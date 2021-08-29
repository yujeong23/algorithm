import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    square = list(map(int,input().split()))
    cnt = [0] * 100
    for i in square:
        cnt[i] += 1
    for idx in range(100):
        if cnt[idx] % 2:
            result = idx
            break

    print('#{} {}'.format(tc, result))
