"""
10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램
각 수는 0 이상 10000 이하의 정수
"""
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    result = 0
    for num in nums:
        if num % 2:
            result += num


    print('#{} {}'.format(tc, result))