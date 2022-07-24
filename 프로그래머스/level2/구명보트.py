from collections import deque

def solution(people, limit):
    answer = 0
    q = deque(sorted(people))
    
    while q:
        cur = q.pop()
        if q and q[0] + cur <= limit:
            q.popleft()
        answer += 1
        
    return answer