import sys
sys.stdin = open('s_4466_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    scores = sorted(list(map(int,input().split())))              # list 정렬
    max_score = 0

    for idx in range(1, K+1):                                   # 제일 큰 값 K개 더해서 쵀댓값 구하기
        max_score += scores[-idx]

    print('#{} {}'.format(tc, max_score))



# itertools의 조합(combinations)이용
# 런타임에러
from itertools import combinations
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    scores = list(map(int,input().split()))
    max_score = 0

    for score in combinations(scores, K):
        if max_score < sum(score):
            max_score = sum(score)

    print('#{} {}'.format(tc, max_score))
