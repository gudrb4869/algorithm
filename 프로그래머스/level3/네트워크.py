# 유니언 파인드
def solution(n, computers):
    def find(x):
        if parent[x] < 0:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def merge(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parent[a] += parent[b]
            parent[b] = a
            
    parent = [-1 for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j]:
                merge(i, j)   
    return len([p for p in parent if p < 0])

# DFS
def solution(n, computers):
    answer = 0
    visited = [0] * n
    def dfs(start):
        stack = [start]
        while stack:
            i = stack.pop()
            if not visited[i]:
                visited[i] = 1
            for j in range(n):
                if computers[i][j] and not visited[j]:
                    stack.append(j)

    i = 0
    while 0 in visited:
        if not visited[i]:
            dfs(i)
            answer += 1
        i += 1
    return answer