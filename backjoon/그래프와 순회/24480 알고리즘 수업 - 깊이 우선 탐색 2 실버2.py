import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 1
def dfs(x):
    global count
    visited[x] = count
    count += 1
    for i in sorted(graph[x], reverse=True):
        if visited[i] == 0:
            dfs(i)

dfs(r)
for v in visited[1:]:
    print(v)