# import sys
# sys.stdin = open('input.txt')

N = int(input())
lst = []
for i in range(N+1):
    lst.append(2**i)

print(*lst)