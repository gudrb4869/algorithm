from collections import deque
INF = 10**9
n, k = map(int, input().split())
dist = [INF] * 100001
q = deque()
dist[n] = 0
q.append(n)

def bfs():
    while q:
        x = q.popleft()
        if x == k:
            return dist[k]
        for nxt in (x-1, x + 1, x * 2):
            if 0 <= nxt <= 100000 and dist[x] + 1 < dist[nxt]:
                dist[nxt] = dist[x] + 1
                q.append(nxt)

print(bfs())