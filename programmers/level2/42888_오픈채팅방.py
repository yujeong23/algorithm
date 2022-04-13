def solution(record):
    answer = []
    users = {}
    for r in record:
        if 'Enter' in r or 'Change' in r:
            word, id, name = map(str, r.split())
            users[id] = name
    for re in record:
        if 'Change' not in re:
            if 'Enter' in re:
                word, id, name = map(str, re.split())
                res = f'{users[id]}님이 들어왔습니다.'
            elif 'Leave' in re:
                word, id= map(str, re.split())
                res = f'{users[id]}님이 나갔습니다.'
            answer.append(res)

    return answer
