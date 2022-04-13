def solution(record):
    answer = []
    users = {}
<<<<<<< HEAD
    for r in record:                                        # 바뀐 이름 미리 저장
        if 'Enter' in r or 'Change' in r:
            word, id, name = r.split()
=======
    for r in record:
        if 'Enter' in r or 'Change' in r:
            word, id, name = map(str, r.split())
>>>>>>> e0ab8e703252d8ad710729512d780f4da6a54faf
            users[id] = name
    for re in record:
        if 'Change' not in re:
            if 'Enter' in re:
<<<<<<< HEAD
                word, id, name = re.split()
                res = f'{users[id]}님이 들어왔습니다.'
            elif 'Leave' in re:
                word, id = re.split()
=======
                word, id, name = map(str, re.split())
                res = f'{users[id]}님이 들어왔습니다.'
            elif 'Leave' in re:
                word, id= map(str, re.split())
>>>>>>> e0ab8e703252d8ad710729512d780f4da6a54faf
                res = f'{users[id]}님이 나갔습니다.'
            answer.append(res)

    return answer
<<<<<<< HEAD

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
=======
>>>>>>> e0ab8e703252d8ad710729512d780f4da6a54faf
