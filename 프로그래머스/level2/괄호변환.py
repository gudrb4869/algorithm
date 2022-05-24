def solution(p):
    def swap(target):
        result = ''
        for t in target:
            if t == '(':
                result += ')'
            elif t == ')':
                result += '('
        return result
    
    dic = {"(" : ")", ")" : "("}
    
    if p == '':
        return p

    u, v = '', ''
    
    stack = []
    for i, c in enumerate(p):
        if stack and stack[-1] == dic[c]:
            stack.pop()
            if not stack:
                u = p[:i+1]
                v = p[i+1:]
                break
        else:
            stack.append(c)
            
    stack = []
    for a in u:
        if a == '(':
            stack.append(a)
        elif a == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return '(' + solution(v) + ')' + swap(u[1:-1])
    
    return u + solution(v)