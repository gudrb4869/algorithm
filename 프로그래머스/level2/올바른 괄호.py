def solution(s):
    answer = True
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                answer = False
                break
            stack.pop()   

    return answer and not stack