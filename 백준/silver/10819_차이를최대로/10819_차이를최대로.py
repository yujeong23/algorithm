import sys
from itertools import permutations
sys.stdin=open('input.txt')

def cal(j):
    global maxv
    answer = 0
    for i in range(N-1):
        answer += abs(result[j][i] - result[j][i+1])
    if maxv < answer:
        maxv = answer


N = int(input())
lst = list(map(int,input().split()))
result = list(permutations(lst, N))
maxv = 0
for j in range(len(result)):
    cal(j)
print(maxv)