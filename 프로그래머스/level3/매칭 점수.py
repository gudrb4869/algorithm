import re
from collections import defaultdict

def solution(word, pages):
    word = word.lower()
    dic = defaultdict()
    for page in pages:
        key = re.search('<meta property="og:url" content="(\S+)"/>', page).group(1)
        dic[key] = [0, 0, []]
    
    keys = dic.keys()
    
    for page in pages:
        key = re.search('<meta property="og:url" content="(\S+)"/>', page).group(1)
        dic[key][0] = re.findall(r'[a-z]+', page.lower()).count(word)
        link = re.findall('<a href="(\S+)">', page)
        dic[key][1] = len(link)
        for l in link:
            if l in keys:
                dic[l][2].append(key)
        
    answer = []
    for i, key in enumerate(keys):
        sum = dic[key][0]
        for out in dic[key][2]:
            if out in keys:
                sum += dic[out][0] / dic[out][1]
        answer.append((i, sum))
    answer.sort(key=lambda x : (-x[1], x[0]))
    return answer[0][0]