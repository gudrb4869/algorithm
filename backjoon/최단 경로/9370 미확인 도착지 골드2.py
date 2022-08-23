import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    dist = [INF] * (n + 1)
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
    return dist

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    result = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])

    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)
    for _ in range(t):
        x = int(input())
        if dist_s[x] == dist_s[g] + dist_g[h] + dist_h[x] or dist_s[x] == dist_s[h] + dist_h[g] + dist_g[x]:
            result.append(x)
    print(*sorted(result))