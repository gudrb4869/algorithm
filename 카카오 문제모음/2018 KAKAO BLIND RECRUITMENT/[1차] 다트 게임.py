def solution(dartResult):
    stack = []
    num = 0
    for c in dartResult:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '*':
            stack[-1] *= 2
            if len(stack) > 1:
                stack[-2] *= 2
        elif c == '#':
            stack[-1] *= -1
        else:
            if c == 'D':
                num **= 2
            elif c == 'T':
                num **= 3
            stack.append(num)
            num = 0
    return sum(stack)