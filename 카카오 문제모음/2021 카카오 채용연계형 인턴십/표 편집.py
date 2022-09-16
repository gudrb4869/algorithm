def solution(n, k, cmd):
    result = ['O'] * n
    dic = {0:[None, 1], n-1:[n-2, None]}
    stack = []
    cur = k
    for i in range(1, n - 1):
        dic[i] = ([i - 1, i + 1])
    for c in cmd:
        c = c.split()
        if c[0] == 'U':
            for i in range(int(c[1])):
                cur = dic[cur][0]
        elif c[0] == 'D':
            for i in range(int(c[1])):
                cur = dic[cur][1]
        elif c[0] == 'C':
            stack.append((cur, dic[cur]))
            prev, nxt = dic[cur][0], dic[cur][1]
            del(dic[cur])
            if prev is not None:
                dic[prev][1] = nxt
                if nxt is None:
                    cur = prev
            if nxt is not None:
                dic[nxt][0] = prev
                cur = nxt
        else:
            key, value = stack.pop()
            dic[key] = value
            prev, nxt = value[0], value[1]
            if prev is not None:
                dic[prev][1] = key
            if nxt is not None:
                dic[nxt][0] = key
    
    while stack:
        result[stack.pop()[0]] = 'X'
    return ''.join(result)