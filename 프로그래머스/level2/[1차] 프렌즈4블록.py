def solution(m, n, board):
    board = [list(x) for x in board]
    target = True
    while target:
        target = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '.':
                    target.add((i,j))
              
        for i,j in target:
            board[i][j] = board[i][j+1] = board[i+1][j] = board[i+1][j+1] = '.'
            
        for _ in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if board[i+1][j] == '.':
                        board[i+1][j], board[i][j] = board[i][j], board[i+1][j]
        
    return sum(x.count('.') for x in board)