def solution(n, t, m, p):
    def convert_notation(n, base):
        T = '0123456789ABCDEF'
        q, r = divmod(n, base)
        return convert_notation(q, base) + T[r] if q else T[r]
    
    answer = ''
    i = 1
    lst = '0'
    
    while len(lst) < m * t:
        lst += convert_notation(i, n)
        i += 1
    
    i = 0
    while len(answer) < t:
        if i % m == p - 1:
            answer += lst[i]
        i += 1
        
    return answer