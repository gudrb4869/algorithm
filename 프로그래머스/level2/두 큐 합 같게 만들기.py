from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    length = len(q1) + len(q2)
    answer = 0
    while s1 != s2:
        if answer > length + 2:
            return -1
        elif s1 > s2:
            x = q1.popleft()
            s1 -= x
            s2 += x
            q2.append(x)
        elif s1 < s2:
            x = q2.popleft()
            s2 -= x
            s1 += x
            q1.append(x)
        answer += 1             
    return answer