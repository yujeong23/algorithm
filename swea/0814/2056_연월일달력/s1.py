"""
연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면 ”YYYY/MM/DD”형식으로 출력
날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.

연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
일은 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)
"""
import sys
sys.stdin = open('input.txt')

def calender(date):
    year = int(date[:4])
    mon = int(date[4:6])
    day = int(date[6:])
    month_1 = [1, 3, 5, 7, 10, 12]
    month_2 = [4, 6, 9, 11]
    result = [date[:4], date[4:6], date[6:]]

    if mon not in range(1, 13):
        return -1

    if mon == 2 and day in range(1, 29):
        return '/'.join(result)

    elif mon in month_1 and day in range(1, 32):
        return '/'.join(result)

    elif mon in month_2 and day in range(1, 31):
        return '/'.join(result)

    else:
        return -1

T = int(input())
for tc in range(1,T+1):
    date = input()
    print('#{} {}'.format(tc, calender(date)))

