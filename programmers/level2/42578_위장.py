def comb(n, visited, length):
    global answer

    if len(visited) == n:
        for i in range(len(visited)):
            if visited[i] == 1:
                answer +=
    else:
        for idx in range(length):
            if not visited[idx]:
                visited[idx] = 1
                comb(n, visited, length)
                visited[idx] = 0

def solution(clothes):
    answer = 0
    dict = {}
    for value, key in clothes:
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1

    lst = list(dict.values())

    for i in range(len(lst)):
        visited = [0] * len(lst)
        comb(i, visited, len(lst))
    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))