from collections import defaultdict

def solution(record):
    result = []
    dic = defaultdict(str)
    message = {'Enter' : '님이 들어왔습니다.',
              'Leave' : '님이 나갔습니다.'}
              
    for r in record:
        lst = r.split()
        if lst[0] in ['Enter', 'Change']:
            dic[lst[1]] = lst[2]
    
    for r in record:
        lst = r.split()
        if lst[0] != 'Change':
            result.append(dic[lst[1]] + message[lst[0]])
            
    return result