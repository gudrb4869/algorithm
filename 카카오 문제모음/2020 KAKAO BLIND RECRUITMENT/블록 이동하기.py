from collections import deque

def solution(board):
    n = len(board)
    arr = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            arr[i + 1][j + 1] = board[i][j]
            
    delta = ((1, 0), (0 ,1), (-1, 0), (0, -1))
    q = deque([(1, 1, 1, 2, 0)])
    visited = set([(1, 1, 1, 2)])
    while q:
        r1, c1, r2, c2, t = q.popleft()
        if r1 == c1 == n or r2 == c2 == n:
            return t
        
        cand = []
        for dr, dc in delta:
            nr1, nc1 = r1 + dr, c1 + dc
            nr2, nc2 = r2 + dr, c2 + dc
            if arr[nr1][nc1] == arr[nr2][nc2] == 0:
                cand.append((nr1, nc1, nr2, nc2))
        
        if r1 == r2:
            for d in (-1, 1):
                if arr[r1 + d][c1] == arr[r2 + d][c2] == 0:
                    cand.append((r1, c1, r1 + d, c1))
                    cand.append((r2, c2, r2 + d, c2))
        else:
            for d in (-1, 1):
                if arr[r1][c1 + d] == arr[r2][c2 + d] == 0:
                    cand.append((r1, c1, r1, c1 + d))
                    cand.append((r2, c2, r2, c2 + d))
        
        for nxt in cand:
            if nxt not in visited:
                visited.add(nxt)
                q.append((*nxt, t + 1))