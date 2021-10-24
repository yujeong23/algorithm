import sys
sys.stdin=open('input.txt')

def rotate(arr):
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][N-i-1] = arr[i][j]
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    a = rotate(arr)
    b = rotate(a)
    c = rotate(b)

    print('#{}'.format(tc))
    for x in range(N):
        print(''.join(map(str, a[x])), ''.join(map(str, b[x])), ''.join(map(str, c[x])))