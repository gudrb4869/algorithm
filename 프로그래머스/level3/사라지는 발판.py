def solution(board, aloc, bloc):
    def dfs(board, a, b, turn, count):
        n, m = len(board), len(board[0])
        flag = True
        r1, c1 = a
        r2, c2 = b
        winner, loser = [], []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if turn:
                nr1, nc1 = r1 + dr, c1 + dc
                if 0 <= nr1 < n and 0 <= nc1 < m and board[r1][c1] == 1 and board[nr1][nc1] == 1:
                    flag = False
                    board[r1][c1] = 0
                    cnt, whoWin = dfs(board, [nr1, nc1], b, False, count + 1)
                    if whoWin:
                        winner.append(cnt)
                    else:
                        loser.append(cnt)
                    board[r1][c1] = 1
            else:
                nr2, nc2 = r2 + dr, c2 + dc
                if 0 <= nr2 < n and 0 <= nc2 < m and board[r2][c2] == 1 and board[nr2][nc2] == 1:
                    flag = False
                    board[r2][c2] = 0
                    cnt, whoWin = dfs(board, a, [nr2, nc2], True, count + 1)
                    if whoWin:
                        loser.append(cnt)
                    else:
                        winner.append(cnt)
                    board[r2][c2] = 1
        if flag:
            return (count, not turn)
        else:
            if winner:
                return (min(winner), turn)
            else:
                return (max(loser), not turn)
    
    return dfs(board, aloc, bloc, True, 0)[0]