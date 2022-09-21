from collections import deque
from copy import deepcopy

def jump(r, c, dr, dc, board):
    nr, nc = r + dr, c + dc
    if 0 <= nr < 4 and 0 <= nc < 4:
        if board[nr][nc] == 0:
            return jump(nr, nc, dr, dc, board)
        else:
            return nr, nc
    else:
        return r, c

def check(board):
    result = 0
    for b in board:
        result += sum(b)
    return result == 0

def solution(board, r, c):
    q = deque([(r, c, 0, (), deepcopy(board))])
    delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
    visited = []
    while q:
        r, c, t, state, board = q.popleft()
        if check(board):
            return t
        if (r, c, state, board) in visited:
            continue
        visited.append((r, c, state, deepcopy(board)))
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 4 and 0 <= nc < 4:
                q.append((nr, nc, t + 1, state, deepcopy(board)))
            nr, nc = jump(r, c, dr, dc, board)
            if (nr,nc) != (r,c):
                q.append((nr, nc, t + 1, state, deepcopy(board)))
        
        if board[r][c] != 0:
            if state == ():
                q.append((r, c, t + 1, (r, c), deepcopy(board)))
            else:
                tr, tc = state
                if (r, c) != state and board[r][c] == board[tr][tc]:
                    board[r][c] = board[tr][tc] = 0
                    q.append((r, c, t + 1, (), deepcopy(board)))