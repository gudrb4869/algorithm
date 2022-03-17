from collections import deque
n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]
Min = Max = graph[0][0]
for i in range(n):
    Min = min(Min, min(graph[i]))
    Max = max(Max, max(graph[i]))
answer = 0
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
def bfs(x):
    global answer
    q = deque()
    visit = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visit[i][j] and graph[i][j] > x:
                q.append((i,j))
                cnt += 1
                while q:
                    r, c = q.popleft()
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0<=nr<n and 0<=nc<n:
                            if not visit[nr][nc] and graph[nr][nc] > x:
                                visit[nr][nc] = 1
                                q.append((nr, nc))
    answer = max(answer, cnt)

for x in range(Min - 1, Max):
    bfs(x)
print(answer)