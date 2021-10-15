import sys
sys.stdin = open('input.txt')

N = int(input())
str_N = list(map(str, range(1, N+1)))
clap = ['3', '6', '9']
result = []

for num in str_N:
    cnt = 0
    for i in num:
        if i in clap:
            cnt += 1
    if cnt:
        num = '-'*cnt
    result.append(num)
print(*result)


