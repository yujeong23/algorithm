import sys
sys.stdin = open('input.txt')

# 테스트 케이스가 10개
T = 10
for tc in range(1, T+1):
    N = int(input())
    H = list(map(int, input().split()))
    result = 0
    # 양 끝의 두 칸에는 건물이 지어지지 않으므로 범위를 (2, N-2)로 설정
    for i in range(2, N-2):
        # 현재 건물을 제외하고 양쪽 거리가 2인 건물들 중 가장 높은 건물의 높이 구하기
        # 현재 건물이 양쪽 거리 2인 건물들 중 가장 높은 건물이라면 높이 차이(조망권 확보된 세대수)를 저장
        # 그렇지않으면 조망권이 확보된 세대가 없다는 것이므로 저장하지 않는다
        height = max([H[i - 2], H[i - 1], H[i + 1], H[i + 2]])
        if H[i] > height:
            result += H[i] - height

    print(f'#{tc} {result}')