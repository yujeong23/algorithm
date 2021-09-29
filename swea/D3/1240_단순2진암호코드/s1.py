import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    r, c = map(int, input().split())            # 암호 코드 규칙 딕셔너리로 설정
    code_num = { '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9 }

    codes = []
    for _ in range(r):                  # 배열 중에 1이 포함되어있을 때만 리스트에 추가 ( 없다면 암호가 없는 배열이므로)
        nums = input()
        if '1' in nums:
            codes.append(nums)

    code = codes[0]                     # 암호코드가 있는 배열들은 모두 같은 배열이므로 그 중 하나의 배열만 사용
    result = []

    for idx in range(len(code)-1, -1, -1):      # 배열의 뒤의 숫자부터 확인하면서 숫자가 1이면 암호 코드의 마지막 숫자 의미
        if code[idx] == '1':                    # 암호코드가 시작하는 인덱스 찾기
            start = idx-55
            break

    for num in range(start, start+56, 7):        # 암호코드를 7자리씩 끊어서 딕셔너리에서 확인
        result.append(code_num[code[num:num+7]])


    odd, even = 0, 0
    for idx in range(4):                        # 상품고유번호의 인덱스에 따라 홀수자리, 짝수자리 따로 계산
        odd += result[2*idx]
        even += result[2*idx+1]

    answer = odd*3 + even
    if answer % 10:                             # 고유번호를 정해진 규칙에 따라 계산한 값이 10의 배수인지 확인
        print('#{}'.format(tc), 0)
    else:
        print('#{}'.format(tc), odd+even)

