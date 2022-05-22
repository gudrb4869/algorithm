from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    lst = defaultdict(list)
    dict = defaultdict(int)
    result = defaultdict(int)
    
    for r in set(report):
        src, dst = r.split(' ')
        lst[dst].append(src)
        dict[dst] += 1
    
    for d in dict:
        if dict[d] >= k:
            for s in lst[d]:
                answer[id_list.index(s)] += 1      
    
    return answer