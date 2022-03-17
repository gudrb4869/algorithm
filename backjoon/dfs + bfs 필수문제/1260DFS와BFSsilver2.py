import collections

def dfs(x):
    visited[x] = 1
    print(x, end=' ')
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue = collections.deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        i = queue.popleft()
        if visited[i]:
            print(i ,end=' ')
            for j in graph[i]:
                if not visited[j]:
                    visited[j] = 1
                    queue.append(j)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(1, n + 1):
    graph[i].sort()

dfs(v)
print()
visited = [0] * (n + 1)
bfs(v)