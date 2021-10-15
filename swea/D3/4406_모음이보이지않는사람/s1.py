import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    vowel = ['a', 'e', 'i' , 'o' ,'u']
    words = input()
    result = ''
    for word in words:
        if word not in vowel:
            result += word

    print('#{} {}'.format(tc,result))