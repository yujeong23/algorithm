import sys
sys.stdin = open('input.txt')

a, b = map(int,input().split())
# a-b의 절댓값을 이용해서 구분
# 뺸 값이 0이면 같은 값이므로 '비김'출력
# 뺀 값이 1이면 큰 쪽이 이긴 경우이기 때문에 더 큰 값인 사람 출력
# 뺸 값이 2이면( 0,1 이외의 값)이면 작은 쪽이 이긴 경우이기 때문에 더 작은 값인 사람 출력
if not abs(a-b):
    print('비김')
elif abs(a-b) == 1:
    if a > b:
        print('A')
    else:
        print('B')
else:
    if a > b:
        print('B')
    else:
        print('A')