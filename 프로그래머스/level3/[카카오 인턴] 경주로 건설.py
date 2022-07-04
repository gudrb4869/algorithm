from collections import deque
from math import inf

def solution(board):
    n = len(board)
    result = [[inf] * n for _ in range(n)]
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
    q = deque([(0, 0, None, 0)])
    result[0][0] = 0
    answer = inf
    while q:
        r, c, d, cost = q.popleft()
        if r == n - 1 and c == n - 1 and answer > cost:
            answer = cost
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                n_cost = cost + (100 if d == None or d == k else 600)
                if result[nr][nc] >= n_cost:
                    result[nr][nc] = n_cost
                    q.append((nr, nc, k, n_cost))

    return answer