import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = map(int,input().split())
    palindrome = []
    cnt = 0
    # 범위 안에서 회문인 수들을 리스트에 추가(int형태)
    # 슬라이싱 사용하기 위해서 str로 변경
    for num in range(A, B+1):
        if str(num) == str(num)[::-1]:
            palindrome.append(num)

    # A, B의 범위가 1000이하이므로 제곱근으로 가질 수 있는 값은 32미만의 정수
    # 제곱근이 정수인지 확인 후에 정수이면 위와 같은 방법으로 str형태로 바꾼 후에 회문인지 확인
    # 제곱근도 회문이라면 cnt개수 늘리기
    for p in palindrome:
        for n in range(32):
            if n == p**(1/2):
                sq_num = str(n)
                if sq_num == sq_num[::-1]:
                    cnt += 1

    print('#{} {}'.format(tc, cnt))