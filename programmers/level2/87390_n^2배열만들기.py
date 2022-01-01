def solution(n, left, right):
    # answer = [0] * (n*n)
    # k = 0
    # for i in range((left//n)+1, (right//n)+2):
    #     for j in range(i, n+1):
    #         if i == j:
    #             answer.extend([i] * i)
    #         else:
    #             answer.append(j)
    #
    # return answer[left:right+1]
    answer = []
    left_x, left_y = left//n, left % n
    right_x, right_y = right//n, right % n

n, left, right = 3, 2, 5
print(solution(n, left, right))