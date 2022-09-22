from collections import defaultdict
from math import ceil

def solution(fees, records):
    dic = defaultdict(list)
    total_times = defaultdict(int)
    for r in records:
        t, n, s = r.split()
        t = int(t[:2]) * 60 + int(t[3:])
        dic[n].append((t, -1 if s == 'IN' else 1))
    keys = dic.keys()
    for key in keys:
        time = 0
        if len(dic[key]) % 2 == 1:
            time += 1439
        for t, s in dic[key]:
            time += t * s
        total_times[key] = time
        
    result = []
    for key in keys:
        cost = fees[1]
        if total_times[key] > fees[0]:
            cost += ceil((total_times[key] - fees[0]) / fees[2]) * fees[3]
        result.append((key, cost))
    return list(map(lambda x: x[1], sorted(result)))