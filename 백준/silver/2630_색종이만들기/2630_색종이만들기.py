import sys
sys.stdin=open('input.txt')

def divide(x, y, N):
    global white, blue

    sum_result = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            sum_result += paper[i][j]


    if sum_result == 0:
        white += 1
        return

    elif sum_result == (N**2):
        blue += 1
        return

    else:
        divide(x, y, N//2)
        divide(x+N//2, y, N//2)
        divide(x, y+N//2, N//2)
        divide(x+N//2, y+N//2, N//2)




N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]

white, blue = 0, 0
divide(0, 0, N)
print(white)
print(blue)