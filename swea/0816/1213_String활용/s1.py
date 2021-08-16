import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    word = input()
    lst = input()

    len_w = len(word)
    len_l = len(lst)

    i = 0
    j = 0
    result = 0
    # word와 lst의 길이를 넘어가지않을 때까지 반복
    # 0번째 인덱스부터 글자 비교 -> 다르면 그 다음에 비교할 부분 -1로 돌아감
    # 같은 글자이던지 상관없이 인덱스에 1이 무조건 추가되도록 설정
    # 만약 같은 글자를 찾았다면 result를 하나 늘리고, 문장 인덱스는 하나 다음으로,
    while i < len_l and j < len_w:
        if lst[i] != word[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == len_w:
            result += 1
            i += 1
            j = 0

    print('#{} {}'.format(tc, result))