import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
K = int(input())
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

def dijkstra(start):
    dist = [INF] * (V + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cur_dist, cur = heapq.heappop(q)
        if dist[cur] < cur_dist:
            continue
        for nxt, nxt_dist in graph[cur]:
            cost = cur_dist + nxt_dist
            if cost < dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    return dist[1:]

for i in dijkstra(K):
    print('INF' if i == INF else i)