from collections import deque, defaultdict
import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = defaultdict(list)
visited = [False] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

a = []
def dfs(x):
    visited[x] = True
    a.append(x)
    for i in sorted(graph[x]):
        if not visited[i]:
            dfs(i)

def bfs():
    visited = [False] * (n + 1)
    q = deque([r])
    visited[r] = True
    result = [r]
    while q:
        u = q.popleft()
        for v in sorted(graph[u]):
            if not visited[v]:
                visited[v] = True
                q.append(v)
                result.append(v)
    return result

dfs(r)
print(*a)
b = bfs()
print(*b)