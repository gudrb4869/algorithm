from collections import defaultdict

def solution(survey, choices):
    answer = list('RCJA')
    target = list('TFMN')
    dic = defaultdict(int)
    for i, s in enumerate(survey):
        if choices[i] == 4:
            continue
        dic[s[0 if choices[i] < 4 else 1]] += abs(choices[i] - 4)
            
    for i in range(4):
        if dic[answer[i]] < dic[target[i]]:
            answer[i] = target[i]
    
    return ''.join(answer)