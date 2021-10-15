import sys
from itertools import combinations
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int,input().split())
    height = list(map(int, input().split()))
    minv = B

    sum_result = []
    for _ in range(1, N+1):                 # 점원들의 조합 모두 구하기
        sum_result += (list(combinations(height, _)))

    for result in sum_result:               # 점원 조합에서 점원의 키 각각 더하기
        if sum(result) >= B:                # 더한 키가 선반보다 높다면
            if abs(sum(result) - B) < minv: # 선반과의 키 차이 비교하기
                minv = sum(result) - B


    print('#{} {}'.format(tc, minv))