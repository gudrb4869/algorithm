from collections import deque

delta = ((1, 0), (-1, 0), (0, 1), (0, -1))

def rotate(puzzle):
    n, m = len(puzzle), len(puzzle[0])
    result = [[0] * n for _ in range(m)]
    for r in range(n):
        for c in range(m):
            result[c][n - 1 - r] = puzzle[r][c]
    return result

def bfs(i, j, arr):
    q = deque([(i, j)])
    n = len(arr)
    arr[i][j] = 0
    lst = []
    while q:
        r, c = q.popleft()
        lst.append([r, c])
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc]:
                arr[nr][nc] = 0
                q.append((nr, nc))
    return lst

def trans(arr):
    r = [a[0] for a in arr]
    c = [a[1] for a in arr]
    min_r, max_r = min(r), max(r)
    min_c, max_c = min(c), max(c)
    m = max_r - min_r + 1
    n = max_c - min_c + 1
    
    trans = [[0] * n for _ in range(m)]
    for x, y in arr:
        trans[x - min_r][y - min_c] = 1
    return trans

def compare(puzzle, hole):
    for _ in range(4):
        if len(hole) == len(puzzle) and len(hole[0]) == len(puzzle[0]) and puzzle == hole:
            return True
        puzzle = rotate(puzzle)
    return False

def solution(game_board, table):
    n = len(game_board)
    answer = 0
    puzzles, holes = [], []
    
    for i in range(n):
        for j in range(n):
            game_board[i][j] = 0 if game_board[i][j] else 1
            
    for i in range(n):
        for j in range(n):
            if table[i][j]:
                puzzles.append(trans(bfs(i, j, table)))
            if game_board[i][j]:
                holes.append(trans(bfs(i, j, game_board)))
    
    while holes:
        for puzzle in puzzles:
            if compare(puzzle, holes[-1]):
                answer += sum(sum(p) for p in puzzle)
                puzzles.remove(puzzle)
                break
        holes.pop()
        
    return answer