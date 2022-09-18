s = '0123456789ABCDEF'

def converse(num, n):
    result = ''
    while num:
        num, mod = divmod(num, n)
        result += s[mod]
    return (list(result[::-1]))
    

def solution(n, t, m, p):
    l = ['0']
    i = 1
    while len(l) < t * m:
        l += converse(i, n)
        i += 1
    answer = ''
    for i in range(t):
        answer += l[i * m + p - 1]
    return answer