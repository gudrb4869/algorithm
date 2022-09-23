import heapq
INF = int(1e8)
def solution(n, paths, gates, summits):
    summits = set(summits)
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    
    q = []
    dist = [INF] * (n + 1)
    for gate in gates:
        dist[gate] = 0
        heapq.heappush(q, (0, gate))
    while q:
        intensity, i = heapq.heappop(q)
        if dist[i] < intensity or i in summits:
            continue
        for j, w in graph[i]:
            time = max(intensity, w)
            if time < dist[j]:
                dist[j] = time
                heapq.heappush(q, (time, j)) 
    return sorted([[summit, dist[summit]] for summit in summits], key=lambda x :(x[1], x[0]))[0]