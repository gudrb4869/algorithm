def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)
    for c in s:
        lst = c.split(',')
        for l in lst:
            if int(l) not in answer:
                answer.append(int(l))
    return answer