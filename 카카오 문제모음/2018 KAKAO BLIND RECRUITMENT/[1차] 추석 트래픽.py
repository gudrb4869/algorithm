from datetime import datetime

def solution(lines):
    logs = []
    for l in lines:
        d, s, t = l.split()
        timestamp = datetime.strptime(d + ' ' + s, "%Y-%m-%d %H:%M:%S.%f").timestamp()
        logs.append((timestamp, -1))
        logs.append((timestamp - float(t[:-1]) + 0.001, 1))
    logs.sort(key=lambda x:(x[0], -x[1]))
    accumulated = 0
    answer = 1
    for i, l1 in enumerate(logs):
        cur = accumulated
        for l2 in logs[i:]:
            if l2[0] - l1[0] > 0.999:
                break
            if l2[1] == 1:
                cur += 1
        answer = max(answer, cur)
        accumulated += l1[1]
    return answer