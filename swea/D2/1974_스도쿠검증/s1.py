import sys
sys.stdin = open('input.txt')

def puzzle():
    for i in range(9):
        row_set = set()
        col_set = set()
        for j in range(9):
            row_set.add(sudoku[i][j])
            col_set.add(sudoku[j][i])
        if len(row_set) != 9 or len(col_set) != 9:
            return 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            rec_set = set()
            for k in range(i, i+3):
                for m in range(j, j+3):
                    rec_set.add(sudoku[k][m])
            if len(rec_set) != 9:
                return 0

    return 1


T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, puzzle()))
