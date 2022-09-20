def check(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    return stack == []

def convert(s):
    result = ''
    for c in s:
        if c == '(':
            result += ')'
        else:
            result += '('
    return result

def func(w):
    if w == '':
        return w
    
    stack = []
    for i, c in enumerate(w):
        if c == '(':
            if stack and stack[-1] == ')':
                stack.pop()
            else:
                stack.append(c)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        if not stack:
            break
            
    u, v = w[:i+1], w[i+1:]
    if check(u):
        return u + func(v)
    else:
        return '(' + func(v) + ')' + convert(u[1:-1])
    
def solution(p):
    return func(p)