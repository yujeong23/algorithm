from collections import deque

def solution(people, limit):
    answer = 0
    deq = deque(sorted(people))
    while deq:
        boat = deq.pop()
        if deq:
            while boat+deq[0] <= limit:
                boat += deq[0]
                deq.popleft()
                if not deq:
                    break
        answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))

# 다른 풀이
# def solution(people, limit) :
#     answer = 0
#     people.sort()
#
#     a = 0
#     b = len(people) - 1
#     while a < b :
#         if people[b] + people[a] <= limit :
#             a += 1
#             answer += 1
#         b -= 1
#     return len(people) - answer