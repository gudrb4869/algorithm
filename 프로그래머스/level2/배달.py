import heapq
from bisect import bisect_right

def solution(N, road, K):
    q = []
    INF = int(1e9)
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    dist = [INF] * (N + 1)
    dist[1] = 0
    heapq.heappush(q, (0, 1))
    while q:
        cur_time, cur_idx = heapq.heappop(q)
        if dist[cur_idx] < cur_time:
            continue
        for next_idx, cost in graph[cur_idx]:
            if cur_time + cost < dist[next_idx]:
                dist[next_idx] = cur_time + cost
                heapq.heappush(q, (dist[next_idx], next_idx))       

    return bisect_right(sorted(dist[1:]), K)