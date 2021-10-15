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

# 슬라이싱 사용해서 연/월/일 나눠줌
# 월,일이 조건에 맞는지(range 사용) 확인하기위해서 int로 변환
# 31일인 달과 30일인 달을 리스트로 만들고 해당 리스트에 포함되어있는지 확인
# 출력될 때 맨 앞자리에 0이 있을 경우에도 생략되지 않고 그대로 출력되기 위해서는 str로 출력 필요
# 그 이외의 조건이 맞지 않는 경우에느 -1 출력
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

