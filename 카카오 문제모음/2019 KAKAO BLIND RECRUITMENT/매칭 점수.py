import re

def solution(word, pages):
    word = word.lower()
    dic = {}
    for i, page in enumerate(pages):
        addr = re.findall('<meta property=\"og:url\" content=\"(\S+)\"/>', page)[0]
        dic[addr] = [0, 0, [], i]
        dic[addr][0] = re.findall(r'[a-z]+', page.lower()).count(word)
    
    keys = dic.keys()
    for page in pages:
        addr = re.findall('<meta property=\"og:url\" content=\"(\S+)\"/>', page)[0]
        link = re.findall('<a href=\"(\S+)\">', page)
        dic[addr][1] = len(link)
        for l in link:
            if l in keys:
                dic[l][2].append(addr)
                
    result = []
    for key in keys:
        point = dic[key][0]
        for l in dic[key][2]:
            point += dic[l][0] / dic[l][1]
        result.append((point, dic[key][3]))
        
    return sorted(result, key=lambda x:-x[0])[0][1]