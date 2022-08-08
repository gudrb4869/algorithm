# 다익스트라 알고리즘
import heapq, sys
input = sys.stdin.readline

INF = int(1e9)
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, input().split())

def dijkstra(start, end):
    dist = [INF] * (N + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cur_dist, cur = heapq.heappop(q)
        if dist[cur] < cur_dist:
            continue
        for nxt, new_dist in graph[cur]:
            cost = cur_dist + new_dist
            if cost < dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    return dist[end]

result = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))
print(result if result < INF else -1)