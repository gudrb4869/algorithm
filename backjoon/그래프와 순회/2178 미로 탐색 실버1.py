from collections import deque

directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque()
q.append((1, 0, 0))
visited[0][0] = True

def bfs():
    while q:
        time, r, c = q.popleft()
        if (r, c) == (n - 1, m - 1):
            return time
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == '1' and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((time + 1, nr, nc))
        
print(bfs())