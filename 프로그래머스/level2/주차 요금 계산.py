from collections import defaultdict, deque
from math import ceil
def solution(fees, records):
    answer = []
    dic = defaultdict(deque)
    
    for record in records:
        time, num, status = record.split()
        dic[num].append([time, status])
    
    for key in sorted(list(dic.keys())):
        if len(dic[key]) % 2 == 1:
            dic[key].append(['23:59', 'OUT'])
            
        sum = 0
        while dic[key]:
            time, status = dic[key].popleft()
            if status == 'IN':
                start = int(time[:2]) * 60 + int(time[3:])
            elif status == 'OUT':
                end = int(time[:2]) * 60 + int(time[3:])
                sum += end - start
        
        cost = fees[1] if sum < fees[0] else fees[1] + ceil((sum - fees[0])/fees[2]) * fees[3]
        answer.append(cost)

    return answer