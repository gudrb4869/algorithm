from collections import defaultdict, deque
n = int(input())
graph = defaultdict(list)
visited = [False] * (n + 1)
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0
q = deque([1])
visited[1] = True
while q:
    u = q.popleft()
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            q.append(v)
            answer += 1

print(answer)