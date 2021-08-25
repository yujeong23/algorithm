import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    words = input()
    # 마디의 최대 길이가 10이므로 10부터 작아지도록 범위 설정
    for j in range(len(words)):
        for i in range(10, 1, -1):
            if words[j:j+i] == words[j+i:j+(2*i)]:
                word = words[j:j+i]
                break
    print('#{} {}'.format(tc, len(word)))