"""
월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.
"""
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    date = list(map(int,input().split()))
    mon_31 = [1, 3, 5, 7, 8, 10, 12]
    mon_30 = [4, 6, 9, 11]

    # 첫번째와 두번째 달이 같은 날이 아니라면
    # 첫번째, 두번째 달에서의 날들 계산
    # 그 사이의 날들 계산해서 더하기
    if date[2] - date[0]:

        day = (32 - date[1]) + date[3]
        if date[0] == 2:
            day -= 3
        elif date[0] in mon_30:
            day -= 1

        for mon in range(date[0]+1, date[2]):
            if mon in mon_31:
                day += 31
            elif mon in mon_30:
                day += 30
            else:
                day += 28

    # 같은 달이라면 두번째 날짜(date[3])에서 첫번째 날짜(date[0])빼기 + 1
    else:
        day = date[3] - date[1] + 1

    print('#{} {}'.format(tc,day))




