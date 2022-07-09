from collections import deque

def ctrlMove(r, c, dr, dc, board):
    nr, nc = r + dr, c + dc
    if 0 <= nr < 4 and 0 <= nc < 4:
        if board[nr * 4 + nc] == '0':
            return ctrlMove(nr, nc, dr, dc, board)
        else:
            return nr, nc
    else:
         return r, c   
            

def solution(board, r, c):
    board = ''.join(str(e) for b in board for e in b)
    delta = ((1, 0), (-1, 0), (0, 1), (0, -1))
    q = deque([(r, c, 0, -1, board)])
    visited = set()
    while q:
        r, c, count, enter, board = q.popleft()
        if board.count('0') == 16:
            return count
        if (r, c, enter, board) in visited:
            continue
        visited.add((r, c, enter, board))
        
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 4 and 0 <= nc < 4:
                q.append((nr, nc, count + 1, enter, board))
            nr, nc = ctrlMove(r, c, dr, dc, board)
            if nr == r and nc == c:
                continue
            q.append((nr, nc, count + 1, enter, board))
        
        cur = r * 4 + c
        if board[cur] != '0':
            if enter == -1:
                q.append((r, c, count + 1, cur, board))
            elif enter != cur and board[enter] == board[cur]:
                board = board.replace(board[enter], '0')
                q.append((r, c, count + 1, -1, board))