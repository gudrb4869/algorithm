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
    count = 1
    q = collections.deque([(r)])
    while q:
        x = q.popleft()
        if visited[x]:
            continue
        visited[x] = count
        count += 1
        for i in sorted(graph[x]):
            if visited[i] == 0:
                q.append(i)
                
bfs()
for v in visited[1:]:
    print(v)