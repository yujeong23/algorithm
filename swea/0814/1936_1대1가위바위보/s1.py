import sys
sys.stdin = open('input.txt')

a, b = map(int,input().split())
if not abs(a-b):
    print('비김')
elif abs(a-b) == 1:
    if a > b:
        print('A')
    else:
        print('B')
else:
    if a > b:
        print('B')
    else:
        print('A')