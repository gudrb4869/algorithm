from datetime import datetime

def solution(lines):
    logs = []
    for line in lines:
        l = line.split()
        timestamp = datetime.strptime(l[0] + ' ' + l[1], '%Y-%m-%d %H:%M:%S.%f').timestamp()
        logs.append((timestamp, -1))
        logs.append((timestamp - float(l[2][:-1]) + 0.001, 1))
    
    accumulated = 0
    max_requests = 1
    logs.sort(key=lambda x:x[0])
    print(logs)
    for i, e1 in enumerate(logs):
        current = accumulated
        print('i =', i)
        print('before accumulated =', accumulated, 'before current =', current)
        for e2 in logs[i:]:
            if e2[0] - e1[0] > 0.999:
                break
            if e2[1] > 0:
                current += e2[1]
        print('after : current', current, 'before : max_requests =', max_requests)
        max_requests = max(max_requests, current)
        accumulated += e1[1]
        print('after max_requests =', max_requests, 'after accumulated =', accumulated)
        
    return max_requests