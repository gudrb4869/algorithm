from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    length = len(q1) + len(q2)
    s1, s2 = sum(q1), sum(q2)
    if (s1 + s2) % 2 == 1:
        return -1
    
    count = 0
    while count <= length + 2:
        if s1 == s2:
            return count
        elif s1 > s2:
            cur = q1.popleft()
            s1 -= cur
            s2 += cur
            q2.append(cur)
            count += 1
        else:
            cur = q2.popleft()
            s2 -= cur
            s1 += cur
            q1.append(cur)
            count += 1
    return -1