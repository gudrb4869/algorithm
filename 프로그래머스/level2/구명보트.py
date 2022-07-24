from collections import deque

def solution(people, limit):
    answer = 0
    q = deque(sorted(people))
    
    while q:
        total = q.pop()
        while q and q[0] + total <= limit:
            total += q.popleft()
        answer += 1
        
    return answer