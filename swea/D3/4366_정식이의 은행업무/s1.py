import sys
sys.stdin = open('input.txt')

# 2진수 한자리 변형된 값 후보
def binary_error(lst):
    can = []
    for i in range(len(lst)):
        tmp = lst[i]
        lst[i] = 1 - lst[i]
        can.append(lst[:])
        lst[i] = tmp
    return can

# n진수 -> 10진수
def toten(lst,n):
    ans = 0
    for i in range(len(lst)):
        ans += lst[len(lst)-1-i]*(n**i)
    return ans

# 3진수 한자리 변형된 값 후보
def trinary_error(lst):
    can = []
    x = {2:[1, 0], 1:[2, 0], 0:[2, 1]}
    for i in range(len(lst)):
        tmp = lst[i]
        for j in range(2):
            lst[i] = x[lst[i]][j]
            can.append(lst[:])
            lst[i] = tmp
    return can


T = int(input())
for tc in range(1, T+1):
    binary = list(map(int, list(input())))
    trinary = list(map(int, list(input())))
    binary_can = binary_error(binary)
    candidate_bi = []
    for c in binary_can:
        candidate_bi.append(toten(c, 2))

    trinary_can = trinary_error(trinary)
    candidate_tri = []
    for c in trinary_can:
        candidate_tri.append(toten(c, 3))

    for i in candidate_tri:
        for j in candidate_bi:
            if i==j:
                print('#{} {}'.format(tc, i))
                break