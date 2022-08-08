# Dijkstra
import heapq
INF = int(1e6)
n, k = map(int, input().split())
q = []
time = [INF] * 100001
time[n] = 0
heapq.heappush(q, [0, n])
while q:
    t, cur = heapq.heappop(q)
    if cur == k:
        print(time[k])
        break
    if time[cur] < t:
        continue
    
    if cur * 2 < 100001 and t < time[cur * 2]:
        time[cur * 2] = t
        heapq.heappush(q, (t, cur * 2))
    if cur - 1 >= 0 and t + 1 < time[cur - 1]:
        time[cur - 1] = t + 1
        heapq.heappush(q, (t + 1, cur - 1))
    if cur + 1 < 100001 and t + 1 < time[cur + 1]:
        time[cur + 1] = t + 1
        heapq.heappush(q, (t + 1, cur + 1))

# BFS
from collections import deque
INF = int(1e6)
n, k = map(int, input().split())
time = [INF] * 100001
visited = [False] * 100001
q = deque([(n, 0)])
visited[n] = True
while q:
    cur, t = q.popleft()
    time[cur] = t
    if cur == k:
        print(time[k])
        break
    for i in (cur * 2, cur - 1, cur + 1):
        if 0 <= i < 100001 and not visited[i]:
            if i == cur * 2:
                q.append((i, t))
            else:
                q.append((i, t + 1))
            visited[i] = True