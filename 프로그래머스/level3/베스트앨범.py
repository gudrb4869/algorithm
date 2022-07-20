from collections import defaultdict

def solution(genres, plays):
    answer = []
    cnt = defaultdict(int)
    dic = defaultdict(list)
    
    for i, v in enumerate(genres):
        cnt[v] += plays[i]
        dic[v].append((plays[i], i))
    
    for key in dic.keys():
        dic[key].sort(key=lambda x: (x[0], -x[1]))
    
    for g, p in sorted(list(cnt.items()), key=lambda x : -x[1]):
        for _ in range(2):
            if not dic[g]:
                break
            answer.append(dic[g].pop()[1])
            
    return answer