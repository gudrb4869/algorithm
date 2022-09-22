def solution(n, info):
    answer = [0] * 11
    maxdiff = 0
    for i in range(1024):
        apeach, lion, cur = 0, 0, n
        result = [0] * 11
        for j, b in enumerate(bin(i)[2:].zfill(10)):
            if b == '0' and info[j] > 0:
                apeach += (10 - j)
            elif b == '1':
                if cur > info[j]:
                    result[j] = info[j] + 1
                    cur -= info[j] + 1
                    lion += (10 - j)
                elif info[j]:
                    apeach += (10 - j)                   
        result[-1] = cur
        
        if maxdiff == lion - apeach:
            for j in reversed(range(11)):
                if result[j] < answer[j]:
                    break
                elif result[j] > answer[j]:
                    answer = result
                    break
        elif maxdiff < lion - apeach:
            maxdiff = lion - apeach
            answer = result
        
    return answer if maxdiff > 0 else [-1]