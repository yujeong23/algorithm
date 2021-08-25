import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    won = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []

    for mon in money:
        result.append(won//mon)
        won %= mon


    print('#{}'.format(tc))
    print(*result)
