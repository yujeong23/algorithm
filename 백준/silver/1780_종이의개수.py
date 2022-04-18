def check(x, y, N):
    global answer
    for i in range(x, x+(N//3)):
        for j in range(y, y+(N//3)):
            if papers[i][j] != papers[x][y]:
                return False
    else:
        if papers[x][y] == -1:
            answers[0] += 1
        elif papers[x][y] == 0:
            answers[1] += 1
        else:
            answers[2] += 1
        return True

def divide(s, e, N):
    if N == 1:
        if papers[s][e] == -1:
            answers[0] += 1
        elif papers[s][e] == 0:
            answers[1] += 1
        else:
            answers[2] += 1
        return
    for r in range(3):
        for c in range(3):
            if not check(s+r*(N//3), e+c*(N//3), N):
                divide(s+r*(N//3), e+c*(N//3), N//3)

N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
answers = [0, 0, 0]
divide(0, 0, N)
for answer in answers:
    print(answer)