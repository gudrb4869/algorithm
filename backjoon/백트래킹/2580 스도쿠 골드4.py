board = [list(map(int, input().split())) for _ in range(9)]
r_check = [[False] * 9 for _ in range(9)]
c_check = [[False] * 9 for _ in range(9)]
rect_check = [[False] * 9 for _ in range(9)]

def find(i, j):
    return (i // 3) * 3 + j // 3

def dfs(x):
    if x == 81:
        for b in board:
            print(*b)
        exit(0)
    
    r, c = divmod(x, 9)
    if not board[r][c]:
        for i in range(9):
            if not (r_check[r][i] or c_check[c][i] or rect_check[find(r, c)][i]):
                r_check[r][i] = c_check[c][i] = rect_check[find(r, c)][i] = True
                board[r][c] = i + 1
                dfs(x + 1)
                board[r][c] = 0
                r_check[r][i] = c_check[c][i] = rect_check[find(r, c)][i] = False
    else:
        dfs(x + 1)
        
for i in range(9):
    for j in range(9):
        if board[i][j]:
            r_check[i][board[i][j] - 1] = c_check[j][board[i][j] - 1] = rect_check[find(i, j)][board[i][j] - 1] = True

dfs(0)