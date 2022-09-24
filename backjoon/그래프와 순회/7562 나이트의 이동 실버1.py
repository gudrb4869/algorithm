from collections import deque

directions = ((1, 2), (2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1), (-1, 2), (-2, 1))

for _ in range(int(input())):
    l = int(input())
    board = [[0] * l for _ in range(l)]
    r, c = map(int, input().split())
    x, y = map(int, input().split())
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        if (r, c) == (x, y):
            print(board[x][y])
            break
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < l and 0 <= nc < l and board[nr][nc] == 0:
                board[nr][nc] = board[r][c] + 1
                q.append((nr, nc))