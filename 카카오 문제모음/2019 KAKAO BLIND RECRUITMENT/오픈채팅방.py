def solution(record):
    dic = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    name = {}
    result = []
    for r in record:
        r = r.split()
        if r[0] != 'Leave':
            name[r[1]] = r[2]
        if r[0] != 'Change':
            result.append((r[1], dic[r[0]]))
    
    return [name[r[0]] + r[1] for r in result]