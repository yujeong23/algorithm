"""
하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램
"""
import sys
sys.stdin = open('input.txt')

N = input()
sum_N = 0
for i in range(len(N)):
    sum_N += int(N[i])
print(sum_N)

# N = int(input())
# result = 0
# while N > 0:
#      result += N % 10
#      N //= 10
# print(result)
