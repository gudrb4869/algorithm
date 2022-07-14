from collections import defaultdict

def solution(info, edges):
    def promising(sheep, wolf, cand):
        if sheep <= wolf:
            return
        
        nonlocal answer
        answer = max(answer, sheep)
        for i, c in enumerate(cand):
            if info[c] == 0:
                promising(sheep + 1, wolf, cand[:i] + dic[c] + cand[i + 1:])
            else:
                promising(sheep, wolf + 1, cand[:i] + dic[c] + cand[i + 1:])
    
    answer = 1
    dic = defaultdict(list)
    for p, c in edges:
        dic[p].append(c)
    
    promising(1, 0, dic[0])
    
    return answer