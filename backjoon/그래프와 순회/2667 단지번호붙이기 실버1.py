from collections import deque
n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []

delta = ((0, 1), (0, -1), (1, 0), (-1, 0))
def bfs(i, j):
    count = 1
    q = deque([(i, j)])
    visited[i][j] = True
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True
                count += 1
    return count

for i in range(n):
    for j in range(n):
        if arr[i][j] and not visited[i][j]:
            result.append(bfs(i, j))
print(len(result))
for r in sorted(result):
    print(r)