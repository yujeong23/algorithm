def solution(n):
    answer = 0
    for i in range(2, n):
        if not (n-1) % i:
            answer = i
            break
    return answer