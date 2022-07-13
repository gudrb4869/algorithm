from collections import deque

def solution(board):
    n = len(board)
    arr = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            arr[i + 1][j + 1] = board[i][j]
            
    dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
    q = deque([(1, 1, 1, 2, 0)])
    visited = set([(1, 1, 1, 2)])
    while q:
        r1, c1, r2, c2, t = q.popleft()
        if r1 == c1 == n or r2 == c2 == n:
            return t
        
        cand = []
        for i in range(4):
            nr1, nc1 = r1 + dr[i], c1 + dc[i]
            nr2, nc2 = r2 + dr[i], c2 + dc[i]
            if arr[nr1][nc1] == 0 and arr[nr2][nc2] == 0:
                cand.append((nr1, nc1, nr2, nc2))
            
        if r1 == r2:
            for d in (-1, 1):
                if arr[r1 + d][c1] == 0 and arr[r2 + d][c2] == 0:
                    cand.append((r1, c1, r1 + d, c1))
                    cand.append((r2, c2, r2 + d, c2))
        else:
            for d in (-1, 1):
                if arr[r1][c1 + d] == 0 and arr[r2][c2 + d] == 0:
                    cand.append((r1, c1, r1, c1 + d))
                    cand.append((r2, c2, r2, c2 + d))
        
        for nxt in cand:
            if nxt not in visited:
                visited.add(nxt)
                q.append((*nxt, t + 1))