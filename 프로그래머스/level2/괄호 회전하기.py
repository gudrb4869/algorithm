from collections import deque

def check(s):
    dic = {')': '(', ']': '[', '}': '{'}
    stack = []
    
    for c in s:
        if c in dic.keys():
            if stack and stack[-1] == dic[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
            
    return not stack

def solution(s):
    answer = 0
    q = deque(s)
    for _ in range(len(s)):
        if check(q):
            answer += 1
        q.rotate(-1)
        
    return answer