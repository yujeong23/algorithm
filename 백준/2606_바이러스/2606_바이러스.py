import sys
sys.stdin = open('input.txt')

num = int(input())
N = int(input())
arr = [[0] * (num+1) for _ in range(num+1)]

for _ in range(N):
    i, j = map(int, input().split())
    arr[i][j] = arr[j][i] = 1

worm = [1]
checked = [1]

while worm:
    i = worm.pop()

    for j in range(1, num + 1):
        if arr[i][j] == 1 and (j not in checked):
            worm.append(j)
            checked.append(j)

print(len(checked)-1)





