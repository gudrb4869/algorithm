from collections import deque
n = int(input())
graph = [list(input()) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
results = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not visit[i][j]:
            q = deque()
            q.append((i, j))
            cnt = 1
            visit[i][j] = 1
            while q:
                r, c = q.popleft()
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < n and 0 <= nc < n:
                        if not visit[nr][nc] and graph[nr][nc] == '1':
                            visit[nr][nc] = 1
                            cnt += 1
                            q.append((nr, nc))
            results.append(cnt)
print(len(results))
for result in sorted(results):
    print(result)