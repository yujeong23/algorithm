# 조합 이용한 풀이 -> tc 1번 통과 x
# def solution(clothes):
#     answer = 0
#     dict = {}
#     for value, key in clothes:
#         if key in dict:
#             dict[key] += 1
#         else:
#             dict[key] = 1
#
#     lst = list(dict.values())
#
#     for i in range(1, len(lst)+1):
#
#         def comb(idx, n):
#             nonlocal answer, visited, lst
#
#             if sum(visited) == n:
#                 cnt = 1
#                 for i in range(len(visited)):
#                     if visited[i]:
#                         cnt *= lst[i]
#                 answer += cnt
#
#             for idx in range(idx, len(lst)):
#                 if not visited[idx]:
#                     visited[idx] = 1
#                     comb(idx+1, n)
#                     visited[idx] = 0
#
#         visited = [0] * len(lst)
#         comb(0, i)
#     return answer

def solution(clothes):
    answer = 1
    dict = {}
    for value, key in clothes:
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 2

    for num in dict.values():
        answer *= num

    return answer-1


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))