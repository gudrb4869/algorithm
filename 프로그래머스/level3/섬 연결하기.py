# 크루스칼 알고리즘. 최소 신장 트리
def solution(n, costs):
    def find(u):
        if u != p[u]:
            p[u] = find(p[u])
        return p[u]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            p[b] = a
        else:
            p[a] = b
            
    answer = 0
    p = [i for i in range(n+1)]
    
    for a, b, cost in sorted(costs, key=lambda x:x[2]):
        if find(a) != find(b):
            union(a, b)
            answer += cost
    
    return answer