"""
입력으로 1개의 정수 N 이 주어진다.
정수 N 의 약수를 오름차순으로 출력하는 프로그램
"""
N = 10
result = []
for num in range(1, N+1):
    if not N % num:
        result.append(num)
print(*result)