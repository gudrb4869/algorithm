def strToInt(s):
    return ((int(s[:4]) - 2000) * 12 + int(s[5:7])) * 28 + int(s[8:])

def solution(today, terms, privacies):
    today = strToInt(today)
    dic = {}
    for t in terms:
        t = t.split()
        dic[t[0]] = int(t[1])
    
    answer = []
    for i, p in enumerate(privacies):
        p = p.split()
        if today > strToInt(p[0]) + dic[p[1]] * 28 - 1:
            answer.append(i + 1)
        
    return answer