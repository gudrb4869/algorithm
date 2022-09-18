def solution(m, n, board):
    answer = 0
    board = [list(board[i]) for i in range(m)]
    while True:
        s = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] != '#':
                    s.add((i, j))
                    s.add((i, j + 1))
                    s.add((i + 1, j))
                    s.add((i + 1, j + 1))
        if not s:
            break
        answer += len(s)
        for i, j in s:
            board[i][j] = '#'
        for _ in range(m):
            for i in range(1, m):
                for j in range(n):
                    if board[i][j] == '#':
                        board[i - 1][j], board[i][j] = board[i][j], board[i - 1][j]
    return answer