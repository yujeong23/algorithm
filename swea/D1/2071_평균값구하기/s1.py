"""
10개의 수를 입력 받아, 평균값을 출력하는 프로그램
"""
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int,input().split()))
    avg = round(sum(nums) / len(nums))
    print('#{} {}'.format(tc,avg))