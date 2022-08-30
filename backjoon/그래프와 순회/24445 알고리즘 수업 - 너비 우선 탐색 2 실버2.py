import sys, collections
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs():
    q = collections.deque([r])
    visited[r] = 1
    count = 2
    while q:
        u = q.popleft()
        for v in sorted(graph[u], reverse=True):
            if visited[v] == 0:
                visited[v] = count
                count += 1
                q.append(v)

bfs()
for v in visited[1:]:
    print(v)