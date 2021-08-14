import sys
sys.stdin = open('input.txt')

alphas = list(map(str,input()))
result = []
for alpha in alphas:
    num = ord(alpha)
    if num < 115:
        result. append(ord(alpha) - 64)
    else:
        result. append(ord(alpha) - 96)

print(*result)
