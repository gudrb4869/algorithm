from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque()
    visited = [[0] * m for _ in range(n)]
    queue.append(iceList[0])
    visited[iceList[0][0]][iceList[0][1]] = 1
    ice = 0
    adj = []
    while queue:
        r, c = queue.popleft()
        ice += 1
        count = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and graph[nr][nc] != 0:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
                elif graph[nr][nc] == 0:
                    count += 1
        if count > 0:
            adj.append((r, c, count))

    for x, y, c in adj:
        graph[x][y] = graph[x][y] - c if graph[x][y] - c > 0 else 0
        if graph[x][y] == 0 and (x, y) in iceList:
            iceList.remove((x, y))

    return ice

n, m = map(int, input().split())
graph, iceList = [list(map(int, input().split())) for _ in range(n)], []
dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            iceList.append((i, j))
time = 0
while 1:
    if len(iceList) != bfs():
        break
    time += 1
    if sum(map(sum, graph)) == 0:
        time = 0
        break

print(time)