import copy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dr = (-1,1,0,0)
dc = (0,0,-1,1)
stack = []
answer = 0

def move(board, idx):
    movedBlock = []
    return board

def dfs(board, cnt):
    global answer
    if cnt >= 5:
        answer = max(answer, max(map(max, board)))
        return
    copyboard = copy.deepcopy(board)
    for i in range(4):
        dfs(move(copyboard, i), cnt + 1)
    return

dfs(board, 0)
print(answer)