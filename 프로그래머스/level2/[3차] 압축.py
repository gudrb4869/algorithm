def solution(msg):
    dic = list('_ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    answer = []
    i = 0
    while i < len(msg):
        cur = ''
        j = i
        
        while j < len(msg):
            if cur + msg[j] not in dic:
                dic.append(cur + msg[j])
                break
            else:
                cur += msg[j]
                j += 1

        answer.append(dic.index(cur))
        i = j
        
    return answer