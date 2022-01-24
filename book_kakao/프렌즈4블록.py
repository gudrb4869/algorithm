'''m, n = map(int, input().split())
board = list(map(str, input().split()))
answer = 0

def dfs(k):
    global answer
    
    i, j = k // m, k % n 
    
    if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
        answer += 4
        dfs(i,j+1)
        dfs(i+1,j)
        dfs(i+1,j+1)

print(dfs(0))'''

m, n = map(int, input().split())
board = list(map(str, input().split()))
board = [list(x) for x in board]

matched = True
while matched:
    matched = []
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] != '#':
                matched.append([i, j])

    for i, j in matched:
        board[i][j] = board[i][j + 1] = board[i + 1][j] = board[i + 1][j + 1] = '#'

    for _ in range(m):
        for i in range(m - 1):
            for j in range(n):
                if board[i + 1][j] == '#':
                    board[i + 1][j], board[i][j] = board[i][j], '#'

print(sum(x.count('#') for x in board))