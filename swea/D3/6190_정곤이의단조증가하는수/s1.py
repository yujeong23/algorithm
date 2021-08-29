import sys
sys.stdin = open('input.txt')

def plus(m):
    while m:
        if (m % 10) >= (m//10) % 10:
            m //= 10
        else:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    multi = []
    result = set()

    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            multi.append(nums[i]*nums[j])

    for m in multi:
        if plus(m):
            result.add(m)

    if len(result):
        maxV = max(result)
    else:
        maxV = -1
    print('#{} {}'.format(tc, maxV))






