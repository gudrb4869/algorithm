from collections import defaultdict

def solution(id_list, report, k):
    result = [0] * len(id_list)
    dic = defaultdict(list)
    for r in set(report):
        src, dst = r.split()
        dic[dst].append(src)
    for key in dic.keys():
        if len(dic[key]) >= k:
            for v in dic[key]:
                result[id_list.index(v)] += 1
    return result