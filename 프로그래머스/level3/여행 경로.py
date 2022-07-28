from collections import defaultdict

def solution(tickets):
    dic = defaultdict(list)
    
    for a, b in sorted(tickets, reverse=True):
        dic[a].append(b)

    route = []
    def dfs(a):
        while dic[a]:
            dfs(dic[a].pop())
        route.append(a)
    
    dfs('ICN')
    return route[::-1]