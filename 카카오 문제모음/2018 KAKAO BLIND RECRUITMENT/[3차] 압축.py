def solution(msg):
    dic = {chr(65 + i): i + 1 for i in range(26)}
    answer = []
    l = 0
    idx = 27
    while l < len(msg):
        r = l
        while r < len(msg) and msg[l:r + 1] in dic:
            r += 1
        if msg[l:r + 1] not in dic:
            dic[msg[l:r + 1]] = idx
            idx += 1
        answer.append(dic[msg[l:r]])
        l = r
            
    return answer