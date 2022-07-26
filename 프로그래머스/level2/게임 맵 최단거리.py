from collections import deque

def solution(maps):
    directions = ((1, 0), (0, 1), (0, -1), (-1, 0))
    m, n = len(maps), len(maps[0])
    visited = [[0] * n for _ in range(m)]
    queue = deque([(0, 0, 1)])
    visited[0][0] = 1
    
    while queue:
        r, c, count = queue.popleft()
        if (r, c) == (m - 1, n - 1):
            return count
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and maps[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                queue.append((nr, nc, count + 1))
    return -1