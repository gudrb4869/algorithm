class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * (n + 1)
        
    def find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            self.parent[a] += self.parent[b]
            self.parent[b] = a

def solution(n, wires):
    answer = 100
    
    for i in range(len(wires)):
        union_find = UnionFind(n)
        for j, (v1, v2) in enumerate(wires):
            if i == j:
                src = v1
                dst = v2
                continue
            union_find.merge(v1, v2)
            
        first = union_find.find(src)
        second = union_find.find(dst)
        answer = min(answer, abs(union_find.parent[first] - union_find.parent[second]))
            
    return answer