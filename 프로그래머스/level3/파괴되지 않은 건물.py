def solution(board, skill):
    N, M = len(board), len(board[0])
    arr = [[0] * (M + 2) for _ in range(N + 2)]
    for t, r1, c1, r2, c2, d in skill:
        arr[r1 + 1][c1 + 1] += -d if t == 1 else d
        arr[r2 + 2][c1 + 1] += d if t == 1 else -d
        arr[r1 + 1][c2 + 2] += d if t == 1 else -d
        arr[r2 + 2][c2 + 2] += -d if t == 1 else d
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            arr[i][j] += arr[i - 1][j]
            
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            arr[i][j] += arr[i][j - 1]

    count = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if arr[i][j] + board[i - 1][j - 1] > 0:
                count += 1
    return count