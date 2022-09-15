from collections import deque

def solution(board):
    n = len(board)
    cost = [[[int(1e9)] * 4 for _ in range(n)] for _ in range(n)]
    dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
    for i in range(4):
        cost[0][0][i] = 0
    q = deque([(0, 0, 0, 0), (0, 0, 1, 0)])
    while q:
        r, c, d, cur = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not board[nr][nc]:
                new = cur + (100 if d == i else 600)
                if new < cost[nr][nc][i]:
                    cost[nr][nc][i] = new
                    q.append((nr, nc, i, new))
    return min(cost[-1][-1])