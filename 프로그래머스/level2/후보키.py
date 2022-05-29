from itertools import combinations
from collections import defaultdict

def solution(relation):
    answer = []
    target = [i for i in range(len(relation[0]))]
    
    for i in range(1, len(relation[0]) + 1):
        dic = defaultdict(set)
        idx = list(combinations(target, i))
        
        for rel in relation:
            for j, comb in enumerate(list(combinations(rel, i))):
                dic[j].add(comb)
        
        for key in dic.keys():
            if len(dic[key]) == len(relation):
                check = 0
                for k in range(len(idx[key])):
                    for t in list(combinations(idx[key], k)):
                        if t in answer:
                            check = 1
                            break
                if not check:
                    answer.append(idx[key])
        
    return len(answer)