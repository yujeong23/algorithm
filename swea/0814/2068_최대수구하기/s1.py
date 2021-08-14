"""
10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램
"""
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int,input().split()))
    max_num = nums[0]
    for num in nums:
        if max_num < num:
            max_num = num

    print('#{} {}'.format(tc, max_num))