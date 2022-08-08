# 모든 테케 x
def solution(name):
    if set(name) == 'A':
        return 0
    new = name
    answer = 0
    for cnt in range(19, 1, -1):
        alpha = 'A' * cnt
        if alpha in name:
            new = name.replace(alpha, 'A')
    minv = len(name) - 1
    for idx in range(len(new)):
        if new[idx] == 'A':
            temp = 2 * (idx-1) + len(new) - idx - 1
            minv = min(temp, minv)
        num = ord(new[idx])-65
        if num > 13:
            answer += 26 - num
        else:
            answer += num

    answer += minv
    return answer

print(solution(	"JEROEN"))
print(solution("JAN"))
print(solution("AAB"))