from math import ceil

def solution(progresses, speeds):
    answer = []
    rest = []
    for p, s in zip(progresses, speeds):
        rest.append(ceil((100 - p) / s))
        
    cur = 0
    for i in range(len(rest)):
        if cur >= rest[i]:
            answer[-1] += 1
        else:
            answer.append(1)
            cur = rest[i]
            
    return answer