from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    queue = deque([1])
    visited[1] = True

    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)
    
    return dist.count(max(dist))