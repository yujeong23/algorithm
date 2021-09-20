import sys
sys.stdin = open('input.txt')

def calculate(num_lst, op_lst):
    global N
    cal_lst = []
    operator = ['+', '-', '*', '//']
    op_result = []
    for _ in range(4):
        op_result += operator[_] * op_lst[_]

    result = num_lst[0]
    def dfs(idx, result):
        nonlocal result
        if idx == N-2:
            cal_lst.append(result)
            return

        if op_result[idx] == '+':
            dfs(idx+1, result+num_lst[idx+1])




N = int(input())
num_lst = list(map(int,input().split()))
op_lst = list(map(int,input().split()))
sorted(num_lst)
print(calculate(num_lst, op_lst))