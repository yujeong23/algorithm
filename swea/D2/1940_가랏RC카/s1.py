"""
RC (Radio Control) 카의 이동거리를 계산하려고 한다.
입력으로 매 초마다 아래와 같은 command 가 정수로 주어진다.
0 : 현재 속도 유지.
1 : 가속
2 : 감속
위 command 중, 가속(1) 또는 감속(2) 의 경우 가속도의 값이 추가로 주어진다.
가속도의 단위는, m/s2 이며, 모두 양의 정수로 주어진다.
입력으로 주어진 N 개의 command 를 모두 수행했을 때, N 초 동안 이동한 거리를 계산하는 프로그램을 작성하라.
RC 카의 초기 속도는 0 m/s 이다.
"""
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    speed = 0
    result = 0

    for i in range(N):
        command = list(map(int,input().split()))
        # 1이면 가속, 2이면 감속
        if command[0] == 1:
            speed += command[1]
        # 현재 속도가 감속할 속도보다 더 작은 경우, 속도는 0m/s
        elif command[0] == 2:
            if speed < command[1]:
                speed = 0
            else:
                speed -= command[1]
        # 1초만큼 이동이기 때문에 이동거리는 속도 *1 을 더하면 된다.
        # 0이어도 기존 속도를 유지하기 때문에 원래의 속도를 더해주면 된다.
        result += speed

    print('#{} {}'.format(tc,result))




