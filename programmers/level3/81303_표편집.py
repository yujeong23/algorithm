def solution(n, k, cmd):
    answer = ['O'] * n
    delete = []
    current = k
    for cm in cmd:
        print(answer)
        print(delete)
        print(current)
        if len(cm) == 1:
            if cm == 'C':
                answer[current] = 'X'
                delete.append(current)
                if current == n-1:
                    while True:
                        if answer[current-1] == 'O':
                            break
                        current -= 1
                    current -= 1
                else:
                    while True:
                        if answer[current+1] == 'O':
                            break
                        current += 1
                    current += 1
            else:
                answer[delete.pop()] = 'O'
        else:
            alpha, num = map(str, cm.split())
            if alpha == 'U':
                while True:
                    if answer[current - int(num)] == 'O':
                        break
                    current -= int(num)
                current -= int(num)
            else:
                while True:
                    if answer[current + int(num)] == 'O':
                        break
                    current += int(num)
                current += int(num)

    return ''.join(answer)

# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))