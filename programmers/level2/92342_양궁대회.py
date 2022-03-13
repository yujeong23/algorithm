import copy
answer = []
maxV = 1

def cal(L, A):
    apeach, lion = 0, 0
    for idx in range(11):
        if A[idx] == 0 and L[idx] == 0:
            continue
        elif A[idx] < L[idx]:
            lion += (10 - idx)
        else:
            apeach += (10 - idx)
    return lion - apeach

def compare(res, L):
    global answer, maxV

    if maxV < res:
        answer = [copy.deepcopy(L)]
        maxV = res
    elif maxV == res:
        answer.append(copy.deepcopy(L))

def solution(n, info):
    global answer

    def score(s, L, cnt):

        if cnt == 11:
            if sum(L) == n:
                compare(cal(L, info), L)

            elif sum(L) < n:
                L[10] += n - sum(L)
                compare(cal(L, info), L)
                L[10] -= n - sum(L)
            return
        for i in range(s, 11):
            L[i] = info[i] + 1
            score(i + 1, L, cnt+1)
            L[i] = 0
            score(i + 1, L, cnt + 1)

    score(0, [0] * 11, 0)

def solution(n, info):
    global answer

    def score(s, L, cnt):

        if not cnt:
            compare(cal(L, info), L)
            return
        if s == 10 and cnt:
            L[10] = cnt
            score(s+1, L, 0)
            L[10] = 0
        else:
            if info[s]+1 <= cnt:
                temp = info[s] + 1
                L[s] = temp
                score(s+1, L, cnt - temp)
                L[s] = 0
            score(s+1, L, cnt)


    score(0, [0] * 11, n)
    if not answer:
        return [-1]
    answer.sort(key=lambda x: x[::-1])
    return answer[-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
