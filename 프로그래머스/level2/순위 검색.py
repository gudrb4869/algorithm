import re, itertools, bisect, collections

def solution(info, query):
    answer = []
    dic = collections.defaultdict(list)
    binarys = list(itertools.product((True, False), repeat=4))
    
    for inf in info:
        inf = inf.split()
        for binary in binarys:
            key = ''.join(inf[i] if binary[i] else '-' for i in range(4))
            dic[key].append(int(inf[4]))
    
    for k in dic.keys():
        dic[k].sort()
    
    for q in query:
        q = re.sub('and ','', q).split()
        key = ''.join(q[0:-1])
        i = bisect.bisect_left(dic[key], int(q[-1]))
        answer.append(len(dic[key])- i)
    return answer