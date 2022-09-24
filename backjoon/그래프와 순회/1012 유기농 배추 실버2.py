from collections import deque
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    answer = 0
    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visited[i][j]:
                answer += 1
                visited[i][j] = True
                q.append((i, j))
                while q:
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))
    print(answer)